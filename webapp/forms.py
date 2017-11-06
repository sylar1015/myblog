#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask_wtf import FlaskForm
from flask_pagedown.fields import PageDownField
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length
from webapp.models import *

class PublishForm(FlaskForm):

    title = StringField('标题', validators=[DataRequired(), Length(min=1, max=128)])
    tags = StringField('标签')
    category = SelectField('分类', coerce=int)
    content = PageDownField('正文', validators=[DataRequired()])
    submit = SubmitField('发布')

    def __init__(self, *args, **kwargs):
        super(PublishForm, self).__init__(*args, **kwargs)
        self.category.choices = \
            [(category.id, category.name) for category in Category.get_all()]

class LoginForm(FlaskForm):

    username = StringField('用户名', 
        validators=[DataRequired(), Length(min=1, max=128)],
        render_kw = {'placeholder': '输入用户名'})
    password = PasswordField('密码',
        validators=[DataRequired(), Length(min=1, max=128)],
        render_kw = {'placeholder': '输入密码'})
    remember_me = BooleanField('记住我')
    submit = SubmitField('登录')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

