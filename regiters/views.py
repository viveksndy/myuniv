from django.shortcuts import render
from django.views.generic import TemplateView
from braces.views import LoginRequiredMixin, AnonymousRequiredMixin
from django.views.generic.edit import FormView, UpdateView
from django.core.urlresolvers import reverse_lazy
from regiters.forms import *
from django.views.generic import TemplateView
# Create your views here.


class Home(TemplateView):
    template_name = "index.html"

class UserDashboardView(TemplateView):
    template_name = "dash.html"

class UserRegistrationView(AnonymousRequiredMixin, FormView):
    template_name = "signup.html"
    authenticated_redirect_url = reverse_lazy(u"home")
    form_class = UserRegistrationForm
    success_url = '/register/user/success/'

    def form_valid(self, form):
        form.save()
        return FormView.form_valid(self, form)

class UserRegistrationSuccessView(TemplateView):
    template_name = "success.html"