from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.views.generic.dates import ArchiveIndexView

from .forms import SnackForm
from .models import Snack


class SnackAV(ArchiveIndexView):
    model = Snack
    date_field = 'create_dt'
    paginate_by = 20


class MonthlySnackLV(ListView):
    model = Snack
    paginate_by = 20
    template_name = 'snack/monthly_list.html'

    def get_context_data(self, **kwargs): # 템플릿 시스템으로 넘겨줄 컨텍스트 변수에 대한 작업
        context = super().get_context_data(**kwargs)
        context['time'] = [self.kwargs['year'], self.kwargs['month']]
        return context

    def get_queryset(self):
        return Snack.objects.filter(supply_year__exact=self.kwargs['year']).filter(supply_month__exact=self.kwargs['month'])


class SnackCV(LoginRequiredMixin, CreateView):
    template_name = 'snack/enroll.html'
    model = Snack
    fields = ('name', 'image', 'url', 'description')
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs): # 템플릿 시스템으로 넘겨줄 컨텍스트 변수에 대한 작업
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['modelForm'] = SnackForm(self.request.POST, self.request.FILES)
        else:
            context['modelForm'] = SnackForm()
        return context
