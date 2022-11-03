from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext as _


class UserManager(BaseUserManager):

    def create_user(self, phone_number, password, **extra_fields):
        """
        Create and save a User with the given username, email and password.
        """

        if not phone_number:
            raise ValueError(_('Users must have an phone_number.'))

        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self, phone_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(
            phone_number=phone_number, password=password, **extra_fields
        )
