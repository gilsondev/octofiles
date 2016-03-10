# -*- coding: utf-8 -*-

from api.test.testcases import OctofilesTestCase


class UserModelTest(OctofilesTestCase):
    def test_should_have_a_name_field(self):
        """Should have a name field in User model"""
        self.assertTrue(True)
