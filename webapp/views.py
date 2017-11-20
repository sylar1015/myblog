#!/usr/bin/env python3
#-*-coding:utf-8-*-

from webapp import app, cache, login_manager
from webapp.forms import *
from webapp.models import *
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from functools import wraps
from flask_login import login_required
from flask_login import login_user, logout_user

@app.route('/')
@cache.cached(timeout=300)
def index():
    posts = Post.get_hotest()
    return render_template('index.html', posts = posts)

@app.route('/about')
@cache.cached(timeout=600)
def about():
    post = Post.get_about()
    return render_template('post.html', post = post)

@app.route('/publish', methods=['GET', 'POST'])
@login_required
def publish():

    form = PublishForm()

    post_id = request.args.get('post_id')

    if form.validate_on_submit():

        title = form.title.data
        tags = form.tags.data
        category_id = form.category.data
        content = form.content.data

        if post_id:
            Post.post_update(post_id=post_id, title=title, tags=tags, category_id=category_id, content=content)
        else:
            Post.post_new(title=title, tags=tags, category_id=category_id, content=content)

        return redirect(redirect_url())

    if post_id:
        post = Post.query.get_or_404(post_id)
        form.title.data = post.title
        form.tags.data = post.tags
        form.category.data = post.category_id
        form.content.data = post.content

    return render_template('publish.html', form = form)

@app.route('/post/<int:post_id>')
@cache.cached(timeout=600)
def post(post_id):
    post = Post.query.get_or_404(post_id)

    post.increase_viewed()

    return render_template('post.html', post = post)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.get_user(username)
        if user and user.verify_password(password):
            login_user(user, form.remember_me.data)
            return redirect(url_for('index'))
        else:
            flash('用户名或密码不正确', category='warning')
    return render_template('login.html', form = form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('用户注销成功', category = 'info')
    return redirect(url_for('index'))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

'''
template util
'''
@app.template_filter('truncate_p')
def truncate_p(string):
    pos = string.find('<hr>')
    if pos < 0:
        return string
    return string[:pos]

@app.context_processor
def utility_processor():
    def latest_posts():
        return Post.get_latest()
    return dict(latest_posts = latest_posts)

'''
util functions
'''
def redirect_url():
    return request.args.get('next') or \
        request.referrer or \
        url_for('index')

'''
decorator
'''
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function
