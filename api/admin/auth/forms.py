# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Required, Email


class LoginForm(Form):
    email = StringField('E-mail', validators=[Required(), Email()])
    password = PasswordField('Senha', validators=[Required()])
    submit = SubmitField('Acessar')
