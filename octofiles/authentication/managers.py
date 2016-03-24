# -*- coding: utf-8 -*-

from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("Usuario precisa de um email valido.")

        if not kwargs.get('name'):
            raise ValueError("Usuario precisa do nome completo.")

        user = self.model(
            email=self.normalize_email(email),
            name=kwargs.get('name')
        )

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(email, password, **kwargs)

        user.is_admin = True
        user.save()

        return user

    def create_owneruser(self, email, password, **kwargs):
        user = self.create_user(email, password, **kwargs)

        user.is_ownerclient = True
        user.save()

        return user

    def admins(self):
        return self.exclude(is_superadmin=True)

    def owner_users(self):
        return self.exclude(is_ownerclient=True)
