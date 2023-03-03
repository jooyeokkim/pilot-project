from django.urls import path

from .api_views import RegisterView, LoginView, UpgradeAuthorityView, DowngradeAuthorityView, QuitView

app_name="api_user"
urlpatterns = [
    # /api/user/register/
    path('register/', RegisterView.as_view()),
    # /api/user/login/
    path('login/', LoginView.as_view()),
    # /api/user/quit/
    path('quit/', QuitView.as_view()),
    # /api/user/upgrade/
    path('upgrade/<int:pk>/', UpgradeAuthorityView.as_view()),
    # /api/user/downgrade/
    path('downgrade/<int:pk>/', DowngradeAuthorityView.as_view()),
]