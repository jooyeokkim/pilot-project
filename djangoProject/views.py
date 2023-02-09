from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from user.forms import SignupForm


class UserCreateView(CreateView):
    template_name='registration/register.html'
    form_class=SignupForm
    success_url=reverse_lazy('register_done')


class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'
