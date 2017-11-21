#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from webapp import db, cache
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, AnonymousUserMixin
from datetime import datetime
from markdown import markdown
import bleach

class User(db.Model, UserMixin):
    
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True, index=True)
    password_hash = db.Column(db.String(256))

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    def __repr__(self):
        return '<User %r>' % self.username

    @staticmethod
    def get_user(username):
        user = db.session.query(User).filter_by(username = username).first()
        return user

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

class Guest(AnonymousUserMixin):
    pass

class Category(db.Model):

    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    link = db.Column(db.String(256))

    posts = db.relationship('Post', backref='category', lazy='dynamic')

    def __repr__(self):
        return '<Category %r>' % self.name

    @staticmethod
    @cache.cached(timeout=7200, key_prefix='Category.get_all')
    def get_all():
        return db.session.query(Category).all()


class Post(db.Model):

    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), index=True)
    link = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime(), default=datetime.now)
    tags = db.Column(db.String(256))
    viewed = db.Column(db.Integer)
    content = db.Column(db.Text)
    content_html = db.Column(db.Text)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    def __repr__(self):
        return '<Post %r>' % self.title

    def get_timestamp(self):
        return self.timestamp.strftime('%Y-%m-%d %H:%M:%S')

    def increase_viewed(self):
        self.viewed += 1
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def on_content_changed(target, value, old_value, initiator):
        allowed_tags = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
                        'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul',
                        'h1', 'h2', 'h3', 'p', 'span', 'hr']

        attr = {
            '*' : ['class'],
            'a' : ['href', 'rel', 'target'],
            'img' : ['src', 'alt']
        }

        target.content_html = bleach.linkify(
            bleach.clean(markdown(value, output_format='html'),
                         tags=allowed_tags,
                         attributes=attr,
                         strip=True))


    @staticmethod
    @cache.cached(timeout=7200, key_prefix='Post.get_about')
    def get_about():
        post = db.session.query(Post).join(Category).filter(Category.name == 'About').first()
        return post

    @staticmethod
    @cache.memoize(600)
    def get_latest(**kwargs):
        num = kwargs.get('num', 3)
        posts = db.session.query(Post).order_by(Post.timestamp.desc()).limit(num).all()
        return posts

    @staticmethod
    @cache.memoize(600)
    def get_hotest(**kwargs):
        num = kwargs.get('num', 10)
        posts = db.session.query(Post).order_by(Post.viewed.desc()).limit(num).all()
        return posts

    @staticmethod
    def post_update(**kwargs):
        post_id = kwargs.get('post_id')
        title = kwargs.get('title')
        tags = kwargs.get('tags')
        content = kwargs.get('content')
        category_id = kwargs.get('category_id')

        post = Post.query.get(post_id)
        post.title = title
        post.tags = tags
        post.content = content
        post.category_id = category_id
        db.session.add(post)
        db.session.commit()

    @staticmethod
    def post_new(**kwargs):
        title = kwargs.get('title')
        tags = kwargs.get('tags')
        content = kwargs.get('content')
        category_id = kwargs.get('category_id')

        item = Post()
        item.title = title
        item.tags = tags
        item.content = content
        item.viewed = 0
        item.timestamp = datetime.now()
        item.category_id = category_id
        db.session.add(item)
        db.session.flush()
        item.link = '/post/%d' % item.id
        db.session.commit()

db.event.listen(Post.content, 'set', Post.on_content_changed)
