from django.urls import path

from snack import api_views

urlpatterns = [
    # /api/snack_request/month_list/
    path('month_list/', api_views.AcceptedMonthListView.as_view()),
]