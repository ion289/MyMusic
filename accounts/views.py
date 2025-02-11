# Create your views here.
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import SignUpForm


class CustomLoginView(LoginView):
    template_name = 'login.html'


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'change_password.html'

    # Pagina la care vom fi trimisi dupa ce resetam parola
    success_url = reverse_lazy('home')


class SignUpView(CreateView):
    template_name = 'signup.html'

    # Formularul standard (creat de Django) pentru creat utilizatori noi
    form_class = SignUpForm

    success_url = reverse_lazy('home')
from django.shortcuts import render

# Create your views here.
