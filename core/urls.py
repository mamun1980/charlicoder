from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="developer.html"), name='about'),
    path('resume/', TemplateView.as_view(template_name="index.html"), name='resume'),
    path('blog/', TemplateView.as_view(template_name="aboutme.html"), name='blog'),
    
    path('contact/', TemplateView.as_view(template_name="contact.html"), name='contact'),
]
