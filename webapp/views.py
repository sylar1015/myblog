#!/usr/bin/env python3
#-*-coding:utf-8-*-

from webapp import app
from webapp.forms import *
from webapp.models import *
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request

@app.route('/')
def index():
    posts = Post.get_hotest()
    return render_template('index.html', posts = posts)

@app.route('/about')
def about():
    post = Post.get_about()
    return render_template('about.html', post = post)

@app.route('/publish', methods=['GET', 'POST'])
def publish():

    form = PublishForm()

    post_id = request.args.get('post_id')

    if form.validate_on_submit():

        title = form.title.data
        tags = form.title.data
        category_id = form.category.data
        content = form.content.data

        if post_id:
            Post.post_update(post_id=post_id, title=title, tags=tags, category_id=category_id, content=content)
        else:
            Post.post_new(title=title, tags=tags, category_id=category_id, content=content)

        return redirect(url_for('index'))

    if post_id:
        post = Post.query.get_or_404(post_id)
        form.title.data = post.title
        form.tags.data = post.tags
        form.category.data = post.category_id
        form.content.data = post.content

    return render_template('publish.html', form = form)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', post = post)

