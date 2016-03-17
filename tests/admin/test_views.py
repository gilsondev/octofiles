# -*- coding: utf-8 -*-
from flask import url_for
from tests.testcases import ClientTestCase
from tests.fixtures import AuthFake


class LoginViewTest(ClientTestCase):
    use_cookies = True

    def setUp(self):
        super(LoginViewTest, self).setUp()
        self.fake = AuthFake()

    def test_get_login(self):
        """GET /login should return status code 200"""
        response = self.client.get(url_for('admin_auth.login'))
        self.assertEquals(200, response.status_code)
        self.assertTrue(b'Login' in response.data)

    def test_post_login(self):
        """POST /login should return status code 302"""
        user = {
            'name': 'Admin',
            'email': 'admin@mail.com',
            'password': 'admintest'
        }
        self.fake.create_user(**user)
        response = self.client.post(url_for('admin_auth.login'), data={
            'email': user['email'],
            'password': user['password']
        })
        self.assertEquals(302, response.status_code)


class DashboardViewTest(ClientTestCase):
    use_cookies = True

    def test_get_dashboard(self):
        """GET /dashboard should reteurn status code 200"""
        response = self.client.get(url_for('admin_auth.dashboard'))
        self.assertEquals(200, response.status_code)
        self.assertTrue(b'Painel Principal' in response.data)
