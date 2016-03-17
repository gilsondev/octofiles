# -*- coding: utf-8 -*-

import forgery_py
from api.models import db
from api.models.user import User


class AuthFake:
    def insert_roles(self):
        pass

    def create_user(self, **kwargs):
        password = kwargs.pop('password')
        user = User(**kwargs)
        user.password = password
        db.session.add(user)
        return user

    def insert_users(self, size=1):
        for item in range(size):
            user = User(
                name=forgery_py.name.full_name(),
                email=forgery_py.email_address(),
                password=forgery_py.lorem_ipsum.word()
            )
            db.session.add(user)
