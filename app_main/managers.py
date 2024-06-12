from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError


class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, password=None):
        if not username:
            raise ValidationError("User must have username")

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, username, password):
        user = self.create_user(first_name, last_name, username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
