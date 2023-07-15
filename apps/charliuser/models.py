from .managers import CustomUserManager
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import User, Group, Permission
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db import models
# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField
mobile = PhoneNumberField(blank=True)


class CharliUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    mobile = PhoneNumberField(blank=True)
    first_name = models.CharField(
        _('First Name'), max_length=50, null=True, blank=True)
    last_name = models.CharField(
        _('First Name'), max_length=50, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
