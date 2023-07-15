from django.urls import path, include
from django.views.generic import TemplateView

from .views import HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('', HomeView.as_view(), name='courses'),
]
