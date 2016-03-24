# -*- coding: utf-8 -*-
from django.db import models
from django_extensions.db import fields as extensions
from octofiles.core.tests import BaseTestCase
from octofiles.core.models import Bucket


class BucketTest(BaseTestCase):
    def test_should_have_field_name(self):
        """Should have field name"""
        self.assertIsInstance(Bucket._meta.get_field('name'),
                              models.CharField)

    def test_should_have_field_client(self):
        """Should have field client"""
        self.assertIsInstance(Bucket._meta.get_field('client'),
                              models.ForeignKey)

    def test_should_have_field_slug(self):
        """Should have field slug"""
        self.assertIsInstance(Bucket._meta.get_field('slug'),
                              extensions.AutoSlugField)

    def test_should_create_a_bucket(self):
        """Should create a bucket"""
        bucket = Bucket.objects.create(
            client=self.oauth_app,
            name=self.oauth_app.name
        )
        self.assertEquals(bucket.pk, 1)
