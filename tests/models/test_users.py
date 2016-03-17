# -*- coding: utf-8 -*-

import pytest
from tests.testcases import BaseTestCase
from tests.fixtures import AuthFake
from api.models.user import User, Role


class UserTestCase(BaseTestCase):
    def setUp(self):
        super(UserTestCase, self).setUp()
        self.fake = AuthFake()

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

    def test_should_have_a_field_role_id(self):
        self.assertTrue(User.__mapper__.has_property('role_id'))

    def test_create_a_user(self):
        user = self.fake.create_user(name="Test", email="test@mail.com",
                                     password="passtest")
        self.assertIsNotNone(user.password_hash)

    def test_should_verify_password(self):
        user = self.fake.create_user(name="Test", email="test@mail.com",
                                     password="passtest")

        self.assertTrue(user.verify_password("passtest"))


class RoleTestCase(BaseTestCase):
    def setUp(self):
        super(RoleTestCase, self).setUp()
        self.fake = AuthFake()

    def test_should_have_a_field_name(self):
        self.assertTrue(Role.__mapper__.has_property('name'))

    def test_should_have_a_field_users(self):
        self.assertTrue(Role.__mapper__.has_property('users'))
