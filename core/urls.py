from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from rest_framework import routers
from apps.charliauth import views

router = routers.DefaultRouter()
router.register(r'charliauth', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    path('', include('apps.resume.urls')),
    path('', include(router.urls)),
    path('home', TemplateView.as_view(template_name='index.html'), name='home'),

    path('auth/', include('apps.charliauth.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('admin/', admin.site.urls),

]
