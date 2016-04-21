# -*- coding: utf-8 -*-

from rest_framework import serializers
from octofiles.core.models import Bucket, Document


class BucketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bucket
        fields = ('name',)


class DocumentSerializer(serializers.ModelSerializer):
    bucket = BucketSerializer()

    class Meta:
        model = Document
