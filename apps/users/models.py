from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, BaseUserManager
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


class User(AbstractUser):
    # email = models.EmailField(_("Email address"), blank=True, unique=True)
    phone_number = models.CharField(max_length=13, blank=False, null=False, unique=True)
    # address = models.TextField(max_length=500, blank=True)
    username = None

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = [] # Email &amp; Password are required by default.

    def __str__(self):
        return self.phone_number

    objects = UserManager()
