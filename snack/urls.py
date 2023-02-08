from django.urls import path
from snack import views

app_name='snack'
urlpatterns = [
    # /snack/enroll/
    path('enroll/', views.snack_create, name='enroll'),
    # /snack/snack_archive/
    path('snack_archive', views.SnackAV.as_view(), name='snack_archive'),
]