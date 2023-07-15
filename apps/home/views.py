from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.translation import gettext_lazy as _


class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = _('Welcome home.....!')
        context["user"] = self.request.user
        return context
