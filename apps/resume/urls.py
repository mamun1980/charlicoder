from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="resume/my-resume.html"), name='resume'),
    path('about-me/', TemplateView.as_view(template_name="developer.html"), name='about'),
    path('resume/', TemplateView.as_view(template_name="index.html"), name='resume'),
    path('blog/', TemplateView.as_view(template_name="aboutme.html"), name='blog'),
    path('login/', TemplateView.as_view(template_name="login.html"), name='login'),
    path('contact/', TemplateView.as_view(template_name="contact.html"), name='contact'),
]
