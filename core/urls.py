from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from django.views.i18n import JavaScriptCatalog

# from rest_framework import routers
# from apps.charliuser import views

# router = routers.DefaultRouter()
# router.register(r'charliuser', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

urlpatterns = [

    path('', include('apps.home.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('user/', include('apps.charliuser.urls')),
    path('', include('apps.resume.urls')),
    path(_('admin/'), admin.site.urls),
    path("pages/", include("django.contrib.flatpages.urls")),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('i18n/', include('django.conf.urls.i18n')),
    path('accounts/', include('allauth.urls')),
]


# urlpatterns += i18n_patterns(
#     path('user/', include('apps.charliuser.urls')),
#     path('', include('apps.resume.urls')),
#     path(_('admin/'), admin.site.urls),
#     path("pages/", include("django.contrib.flatpages.urls")),
#     path('rosetta/', include('rosetta.urls')),

# )
