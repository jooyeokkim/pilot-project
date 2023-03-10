from django.urls import path

from snack import views

app_name='snack'
urlpatterns = [
    # /snack/enroll/
    path('enroll/', views.SnackCV.as_view(), name='enroll'),
    # /snack/snack_archive/
    path('snack_archive/', views.SnackRequestListView.as_view(), name='snack_archive'),
    # /snack/legacy_list/
    path('legacy_list/', views.SnackRequestLegacyListView.as_view(), name='legacy_list'),
    # /snack/monthly_list/
    path('monthly_list/<int:year>/<int:month>/', views.MonthlySnackLV.as_view(), name='monthly_list'),
    # /snack/55/edit/
    path('<int:pk>/edit/', views.SnackEditUV.as_view(), name="edit"),
    # /snack/55/manage/
    path('<int:pk>/manage/', views.SnackManageUV.as_view(), name="manage")
]