from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.views.generic.dates import ArchiveIndexView

from .models import Snack


class SnackLV(ArchiveIndexView):
    model = Snack
    date_field = 'create_dt'
    paginate_by = 20


class MonthlySnackLV(ListView):
    model = Snack
    paginate_by = 20
    template_name = 'snack/monthly_list.html'


class SnackCV(LoginRequiredMixin, CreateView):
    template_name = 'snack/enroll.html'
    model = Snack
    fields = ('name', 'image', 'url', 'description')
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('home')
