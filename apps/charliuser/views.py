from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from rest_framework import viewsets, permissions
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
# from .serializers import CharliUserSerializer, GroupSerializer
from .forms import CharliUserCreationForm


class SignInView(LoginView):
    form_class = AuthenticationForm
    # success_url = '/resume'
    redirect_authenticated_user = True
    template_name = "charliuser/accounts/login.html"

    def get_success_url(self):
        return reverse_lazy('home')

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))


class SignUpView(CreateView):
    form_class = CharliUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'charliuser/accounts/register-v2.html'

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows charliauth to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]