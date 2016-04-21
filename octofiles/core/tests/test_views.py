# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from rest_framework import status
from octofiles.core.tests import BaseTestCase, APIBaseTestCase
from octofiles.core.models import Bucket


class AuthorizationTest(BaseTestCase):
    def test_should_authorizate_the_client(self):
        """Should authorizate the client"""
        self.authenticate()
        self.assertEquals(self.status_code, 200)

    def test_should_generate_a_access_token(self):
        """Should generate a access token"""
        resp = self.authenticate()
        self.assertIsNotNone(resp.get('access_token', None))


class DocumentTest(APIBaseTestCase):
    def setUp(self):
        self.authenticate()
        self.bucket = Bucket.objects.create(
            client=self.oauth_app,
            name=self.oauth_app.name
        )

    def test_should_get_documents(self):
        """Should get documents of client"""
        resp = self.client.get(reverse('api_documents:list',
                                       kwargs={'slug': self.bucket.slug}))
        self.assertEquals(resp.status_code, status.HTTP_200_OK)
