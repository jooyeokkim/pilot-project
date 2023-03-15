from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers

from user import views
from snack.views import SnackRequestListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', SnackRequestListView.as_view(), name='home'),
    path('snack/', include('snack.urls')),
    path('user/', include('user.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.UserCreateView.as_view(), name='register'),
    path('accounts/register/done/', views.UserCreateDoneTV.as_view(), name='register_done'),
    path('accounts/delete/', views.UserDeleteView.as_view(), name='delete'),
]

urlpatterns += [
    path('manage/user/', views.UserListView.as_view(), name='user_list'),
]

router = routers.SimpleRouter()

urlpatterns += [
    path('api/snack_request/', include('snack.api_urls')),
    path('api/user/', include('user.api_urls')),
]

urlpatterns += router.urls
