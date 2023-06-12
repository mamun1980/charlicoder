from django.urls import path
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView


urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    # path("logout/", LogoutView.as_view(), name="logout"),


    # path('login/', TemplateView.as_view(template_name="account/login.html"), name='login'),
    # path('register/', TemplateView.as_view(template_name="charliauth/accounts/register.html"), name='register'),
]
