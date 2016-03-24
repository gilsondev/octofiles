# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from oauth2_provider.models import Application
from model_mommy import mommy
from octofiles.authentication.models import User

GRANT_TYPE_DEFAULT = 'client_credentials'


class BaseTestCase(TestCase):
    """
    Classe que prepara o ambiente de testes para efetuar
    a autenticação e recuperação do token de acesso.
    """
    before_authenticate = False

    @classmethod
    def setUpClass(cls):
        user = mommy.make(User)
        cls.oauth_app = Application.objects.create(
            name="Application Test",
            user=user,
            redirect_uris="",
            authorization_grant_type=Application.GRANT_CLIENT_CREDENTIALS
        )
        super(BaseTestCase, cls).setUpClass()

    def setUp(self):
        if self.before_authenticate:
            self.authenticate()

    def authenticate(self, **kwargs):
        data = {
            'grant_type': kwargs.get('grant_type', GRANT_TYPE_DEFAULT),
            'client_id': kwargs.get('client_id', self.oauth_app.client_id),
            'client_secret': kwargs.get('client_secret',
                                        self.oauth_app.client_secret)
        }
        self.resp = self.client.post(reverse('oauth2_provider:token'), **data)
        return self.resp.json()

    @property
    def status_code(self):
        return self.resp.status_code

    @property
    def response(self):
        return self.resp

    @property
    def access_token(self):
        return self.resp.json['access_token']
