"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers

from user import views
from snack.views import SnackRequestListView
from snack.api_views import SnackRequestViewSet, SnackEmotionViewSet
from user.api_views import UserViewSet

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
    path('api/snack_request/', include('snack.api_urls')),
    path('api/user/', include('user.api_urls')),
]

urlpatterns += [
    path('manage/user/', include('user.urls')),
]

router = routers.SimpleRouter()
router.register('api/snack_request', SnackRequestViewSet)
router.register('api/user', UserViewSet)
router.register('api/snack_emotion', SnackEmotionViewSet)

urlpatterns += router.urls