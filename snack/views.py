from django.views.generic import ListView, UpdateView, FormView, TemplateView

from .form import SnackManageForm, SnackRequestForm, SnackEditForm
from .models import Snack, SnackRequest


# class SnackLV(ArchiveIndexView):
#     model = Snack
#     date_field = 'create_dt'
#     allow_empty = True
#     paginate_by = 20


class SnackRequestListView(TemplateView):
    template_name = "snack/snack_request_list.html"


class SnackRequestLegacyListView(TemplateView):
    template_name = "snack/snack_request_legacy_list.html"


class MonthlySnackLV(ListView):
    model = Snack
    paginate_by = 20
    template_name = 'snack/monthly_list.html'


# class SnackCV(CreateView):
#     template_name = 'snack/enroll.html'
#     model = Snack
#     fields = ('name', 'image', 'url', 'description')


class SnackCV(FormView):
    template_name = 'snack/enroll.html'
    form_class = SnackRequestForm


class SnackEditUV(UpdateView):
    template_name = 'snack/edit.html'
    model = SnackRequest
    form_class = SnackEditForm


class SnackManageUV(UpdateView):
    template_name = 'snack/manage.html'
    model = SnackRequest
    form_class = SnackManageForm
