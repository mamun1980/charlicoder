from django.contrib.auth.backends import ModelBackend
from .models import CharliUser


class EmailMobileBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = CharliUser.objects.get(email=username)
        except CharliUser.DoesNotExist:
            user = CharliUser.objects.get(mobile=username)
        except CharliUser.DoesNotExist:
            return None

        if user.check_password(password):
            return user

    def get_user(self, user_id):
        try:
            return CharliUser.objects.get(pk=user_id)
        except CharliUser.DoesNotExist:
            return None
