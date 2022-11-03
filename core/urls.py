from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', include('apps.resume.urls')),

    path('users/', include('apps.users.urls')),

    path('admin/', admin.site.urls),

]
