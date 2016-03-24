# -*- coding: utf-8 -*-
from django.db import models
from django_extensions.db.fields import AutoSlugField


class Bucket(models.Model):
    client = models.ForeignKey('oauth2_provider.Application',
                               related_name='bucket')
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name')
