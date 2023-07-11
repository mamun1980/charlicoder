from django.shortcuts import render
from django.views.generic import DetailView, TemplateView
from .models import *


class ResumeView(TemplateView):
    template_name = 'resume/index.html'

    def get_context_data(self, **kwargs):
        # import pdb; pdb.set_trace()
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        profile = CandyProfile.objects.get(id=1)
        educations = profile.education_set.all().order_by('passing_year')
        experiences = profile.workexperience_set.all().order_by('-from_date')

        # Add in a QuerySet of all the books
        context["profile"] = profile
        context["educations"] = educations
        context["experiences"] = experiences
        return context
