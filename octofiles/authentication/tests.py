# -*- coding: utf-8 -*-

from django.test import TestCase
from django.db import models
from octofiles.authentication.models import User


class UserModelTest(TestCase):
    def test_should_have_email_field(self):
        """Should have a field 'email'"""
        self.assertIsInstance(User._meta.get_field('email'), models.EmailField)

    def test_should_have_email_be_unique(self):
        """Should have email be unique"""
        field = User._meta.get_field('email')
        self.assertTrue(field.unique)

    def test_should_have_name_field(self):
        """Should have a field 'name'"""
        self.assertIsInstance(User._meta.get_field('name'), models.CharField)

    def test_should_have_name_field_without_blank(self):
        """Should have field 'name' without blank"""
        field = User._meta.get_field('name')
        self.assertFalse(field.blank)

    def test_should_have_is_admin_field(self):
        """Should have a field 'is_admin'"""
        self.assertIsInstance(User._meta.get_field('is_admin'),
                              models.BooleanField)

    def test_should_define_is_admin_with_default_value(self):
        """Should define field 'is_admin' with default value"""
        field = User._meta.get_field('is_admin')
        self.assertFalse(field.default)

    def test_should_have_is_ownerclient_field(self):
        """Should have a field 'is_ownerclient'"""
        self.assertIsInstance(User._meta.get_field('is_ownerclient'),
                              models.BooleanField)

    def test_should_define_is_ownerclient_with_default_value(self):
        """Should define field 'is_ownerclient' with default value"""
        field = User._meta.get_field('is_ownerclient')
        self.assertFalse(field.default)

    def test_should_have_created_at_field(self):
        """Should have a field 'created_at'"""
        self.assertIsInstance(User._meta.get_field('created_at'),
                              models.DateTimeField)

    def test_should_have_updated_at_field(self):
        """Should have a field 'updated_at'"""
        self.assertIsInstance(User._meta.get_field('updated_at'),
                              models.DateTimeField)

    def test_should_create_ownerclient_user(self):
        """Should create a ownerclient user"""
        data = {
            'name': 'Owner User',
            'email': 'owner@mail.com',
            'password': 'owner123'
        }
        user = User.objects.create_owneruser(**data)
        self.assertTrue(user.pk, 1)

    def test_should_create_admin_user(self):
        """Should create a admin user"""
        data = {
            'name': 'Admin User',
            'email': 'admin@mail.com',
            'password': 'admin123'
        }
        user = User.objects.create_superuser(**data)
        self.assertTrue(user.pk, 1)

    def test_should_print_str_representation(self):
        """Should print email in str representation"""
        data = {
            'name': 'Admin User',
            'email': 'admin@mail.com',
            'password': 'admin123'
        }
        user = User.objects.create_superuser(**data)
        self.assertEquals(user.__str__(), 'admin@mail.com')

    def test_should_return_full_name(self):
        """Should a full name"""
        data = {
            'name': 'Admin User',
            'email': 'admin@mail.com',
            'password': 'admin123'
        }
        user = User.objects.create_superuser(**data)
        self.assertEquals(user.get_full_name(), 'Admin User')

    def test_should_return_short_name(self):
        """Should a short name"""
        data = {
            'name': 'Admin User',
            'email': 'admin@mail.com',
            'password': 'admin123'
        }
        user = User.objects.create_superuser(**data)
        self.assertEquals(user.get_short_name(), 'Admin')
