from django.urls import path
from snack import views

app_name='snack'
urlpatterns = [
    # /snack/enroll/
    path('enroll/', views.SnackCV.as_view(), name='enroll'),
    # /snack/snack_archive/
    path('snack_archive/', views.SnackLV.as_view(), name='snack_archive'),
    # /snack/monthly_list
    path('monthly_list/<int:year>/<int:month>', views.MonthlySnackLV.as_view(), name='monthly_list'),
]