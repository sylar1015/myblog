#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from webapp import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, AnonymousUserMixin
from datetime import datetime
from markdown import markdown
import bleach

class Category(db.Model):

    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    link = db.Column(db.String(256))

    posts = db.relationship('Post', backref='category', lazy='dynamic')

    def __repr__(self):
        return '<Category %r>' % self.name

    @staticmethod
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

    @staticmethod
    def on_content_changed(target, value, old_value, initiator):
        allowed_tags = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
                        'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul',
                        'h1', 'h2', 'h3', 'p', 'span']

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
    def get_about():
        post = db.session.query(Post).join(Category).filter(Category.name == 'About').first()
        return post

    @staticmethod
    def get_latest():
        pass

    @staticmethod
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