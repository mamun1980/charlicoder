from django.urls import path
from django.contrib.auth.views import LogoutView
# from django.views.generic import TemplateView

from .views import SignUpView, CharliLoginView

urlpatterns = [
    path('login/', CharliLoginView.as_view(), name='login'),
    path('register/', SignUpView.as_view(), name='register'),
    path("logout/", LogoutView.as_view(next_page='login'), name="logout")
]