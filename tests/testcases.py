# -*- coding: utf-8 -*-
import unittest
from flask import current_app
from api import create_api
from api.models import db


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.api = create_api('testing')
        self.api_context = self.api.app_context()
        self.api_context.push()

        db.create_all()
        self.db = db

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.api_context.pop()

    def test_api_exists(self):
        return self.assertFalse(current_app is None)

    def test_api_is_testing(self):
        return self.assertTrue(current_app.config['TESTING'])
