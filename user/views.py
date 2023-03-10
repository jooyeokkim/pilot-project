from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, RedirectView, FormView

from user.forms import SignupForm


class UserListView(TemplateView):
    template_name = 'user/manage.html'


class UserCreateView(FormView):
    template_name = 'user/register.html'
    form_class = SignupForm


class UserCreateDoneTV(TemplateView):
    template_name = 'user/register_done.html'


class UserDeleteView(LoginRequiredMixin, RedirectView):
    pattern_name = 'home'

    def get(self, request, *args, **kwargs):
        current_user = self.request.user
        current_user.is_active = False
        current_user.save(using='default')
        return super().get(request, *args, **kwargs)
