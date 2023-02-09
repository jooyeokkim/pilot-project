from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from django.views.generic.dates import ArchiveIndexView

from .form import SnackForm
from .models import Snack


class SnackAV(ArchiveIndexView):
    model=Snack
    date_field = 'create_dt'
    paginate_by = 20


class MonthlySnackLV(ListView):
    model=Snack
    paginate_by = 20
    template_name = 'snack/monthly_list.html'

    def get_context_data(self, **kwargs): # 템플릿 시스템으로 넘겨줄 컨텍스트 변수에 대한 작업
        context=super().get_context_data(**kwargs)
        context['time']=[self.kwargs['year'], self.kwargs['month']]
        return context

    def get_queryset(self):
        return Snack.objects.filter(supply_year__exact=self.kwargs['year']).filter(supply_month__exact=self.kwargs['month'])


class SnackCreateView(CreateView):
    template_name='snack/enroll.html'
    form_class=SnackForm


def snack_create(request):
    if request.method == 'POST':
        form = SnackForm(request.POST, request.FILES)
        if form.is_valid():
            snack = form.save(commit=False) # 중복 저장 방지
            snack.save()
            return redirect('home')
    else:
        form = SnackForm() # request.method 가 'GET'인 경우
    context = {'modelForm':form}
    return render(request, 'snack/enroll.html', context)
