# -*- coding: utf-8 -*-
from octofiles.core.tests import BaseTestCase


class AuthorizationTest(BaseTestCase):
    def test_should_authorizate_the_client(self):
        """Should authorizate the client"""
        self.authenticate()
        self.assertEquals(self.status_code, 200)

    def test_should_generate_a_access_token(self):
        """Should generate a access token"""
        resp = self.authenticate()
        self.assertIsNotNone(resp.get('access_token', None))
