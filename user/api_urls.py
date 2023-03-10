from django.urls import path

from .api_views import LoginView

app_name="api_user"
urlpatterns = [
    # /api/user/login/
    path('login/', LoginView.as_view()),
]