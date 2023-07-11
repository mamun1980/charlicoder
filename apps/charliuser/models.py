from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import User, Group, Permission
from django.utils.translation import gettext_lazy as _
from django.db import models
# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField

from .managers import CustomUserManager


class CharliUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    mobile = PhoneNumberField(blank=True)
    groups = models.ManyToManyField(Group, related_name='charli_users')
    user_permissions = models.ManyToManyField(Permission, related_name='charli_users')
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["mobile"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"