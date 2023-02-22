from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, RedirectView, FormView

from user.forms import SignupForm


class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = SignupForm
    success_url = reverse_lazy('register_done')


class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'


class UserDeleteView(LoginRequiredMixin, RedirectView):
    pattern_name = 'home'

    def get(self, request, *args, **kwargs):
        current_user = self.request.user
        current_user.is_active = False
        current_user.save(using = 'default')
        return super().get(request, *args, **kwargs)
