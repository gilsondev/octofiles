# -*- coding: utf-8 -*-

from flask import render_template, redirect, url_for
from flask.ext.login import login_user
from api.models.user import User
from . import admin_auth
from .forms import LoginForm


@admin_auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        login_user(user)
        return redirect(url_for('admin_auth.dashboard'))
    return render_template('auth/login.html', form=form)


@admin_auth.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template('auth/dashboard.html')
