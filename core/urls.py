from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

# from rest_framework import routers
# from apps.charliuser import views

# router = routers.DefaultRouter()
# router.register(r'charliuser', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    path('', include('apps.resume.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('user/', include('apps.charliuser.urls')),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('admin/', admin.site.urls),
    path("pages/", include("django.contrib.flatpages.urls")),

]
