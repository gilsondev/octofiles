# -*- coding: utf-8 -*-
import uuid
from django.db import models
from django_extensions.db import fields as extensions
from octofiles.core.tests import BaseTestCase
from octofiles.core.tests.fake import dummy_file, dummy_image
from octofiles.core.models import Bucket, Document


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


class DocumentTest(BaseTestCase):
    def setUp(self):
        self.bucket = Bucket.objects.create(
            client=self.oauth_app,
            name=self.oauth_app.name
        )

    def test_should_have_field_bucket(self):
        """Should have field bucket"""
        self.assertIsInstance(Document._meta.get_field('bucket'),
                              models.ForeignKey)

    def test_should_have_field_name(self):
        """Should have field name"""
        self.assertIsInstance(Document._meta.get_field('name'),
                              models.CharField)

    def test_should_have_field_file(self):
        """Should have field file"""
        self.assertIsInstance(Document._meta.get_field('file'),
                              models.FileField)

    def test_should_have_field_view(self):
        """Should have field view"""
        self.assertIsInstance(Document._meta.get_field('view'),
                              models.CharField)

    def test_should_have_field_owner(self):
        """Should have field owner"""
        self.assertIsInstance(Document._meta.get_field('owner'),
                              models.UUIDField)

    def test_should_create_a_document_text(self):
        """Should create a document text"""
        fake_file = dummy_file()
        instance = Document.objects.create(
            bucket=self.bucket,
            name="Document Text",
            file=fake_file,
            view=Document.VIEW_CHOICES.private,
            owner=uuid.uuid4()
        )
        self.assertTrue(instance.pk)

    def test_should_create_a_document_image(self):
        """Should create a document image"""
        fake_image = dummy_image()
        instance = Document.objects.create(
            bucket=self.bucket,
            name="Document Image",
            file=fake_image,
            view=Document.VIEW_CHOICES.private,
            owner=uuid.uuid4()
        )
        self.assertTrue(instance.pk)
