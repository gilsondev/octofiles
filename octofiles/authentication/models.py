# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from octofiles.authentication.managers import UserManager


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=80, blank=False)
    is_admin = models.BooleanField(default=False)
    is_ownerclient = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name.split(' ')[0]
