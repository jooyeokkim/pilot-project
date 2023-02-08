from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.views.generic.dates import ArchiveIndexView

from .form import SnackForm
from .models import Snack


class SnackAV(ArchiveIndexView):
    model=Snack
    date_field = 'create_dt'
    paginate_by = 5


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
