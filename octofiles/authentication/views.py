# -*- coding: utf-8 -*-
from octofiles.authentication.models import User
from rest_framework import serializers, viewsets
from oauth2_provider.ext.rest_framework import (
    TokenHasReadWriteScope
)


# first we define the serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer
