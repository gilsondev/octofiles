# -*- coding: utf-8 -*-

import pytest
from tests.testcases import BaseTestCase
from api.models.user import User


class UserTestCase(BaseTestCase):
    def _create_user(self, **kwargs):
        password = kwargs.pop('password')
        user = User(**kwargs)
        user.password = password
        self.db.session.add(user)
        self.db.session.commit()
        return user

    def test_should_have_a_field_name(self):
        self.assertTrue(User.__mapper__.has_property('name'))

    def test_should_have_a_field_email(self):
        self.assertTrue(User.__mapper__.has_property('email'))

    def test_should_have_a_field_password_hash(self):
        self.assertTrue(User.__mapper__.has_property('password_hash'))

    def test_should_have_a_field_password(self):
        user = User()
        with pytest.raises(AttributeError) as exception:
            user.__getattribute__('password')
            self.assertEquals(exception.value.args[0],
                              'Atributo password não é para leitura.')

    def test_create_a_user(self):
        user = self._create_user(name="Test", email="test@mail.com",
                                 password="passtest")
        self.assertIsNotNone(user.password_hash)

    def test_should_verify_password(self):
        user = self._create_user(name="Test", email="test@mail.com",
                                 password="passtest")
        self.assertTrue(user.verify_password("passtest"))
