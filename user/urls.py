from django.urls import path
from user import views

app_name='user'
urlpatterns = [
    # /manage/user/
    path('', views.UserListView.as_view(), name='list'),
]