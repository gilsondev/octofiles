# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import AutoSlugField
from model_utils import Choices


class Bucket(models.Model):
    client = models.ForeignKey('oauth2_provider.Application',
                               related_name='bucket')
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name')

    class Meta:
        db_table = "buckets"

    def __str__(self):
        return self.name


class Document(models.Model):
    VIEW_CHOICES = Choices(
        ('public', _('Public')),
        ('private', _('Private')),
    )
    bucket = models.ForeignKey('Bucket', related_name='documents')
    name = models.CharField(max_length=255)
    file = models.FileField()
    view = models.CharField(max_length=10, choices=VIEW_CHOICES,
                            default=VIEW_CHOICES.public)
    owner = models.UUIDField(max_length=255, blank=True)

    class Meta:
        db_table = "documents"

    def __str__(self):
        return self.name
