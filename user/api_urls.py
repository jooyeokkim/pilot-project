from django.urls import path

from djangoProject.urls import router
from .api_views import LoginView, UserViewSet

app_name="api_user"
urlpatterns = [
    # /api/user/login/
    path('login/', LoginView.as_view()),
]

router.register('api/user', UserViewSet)