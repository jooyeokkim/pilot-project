from django.urls import path

from djangoProject.urls import router
from snack import api_views
from snack.api_views import SnackRequestViewSet, SnackEmotionViewSet

urlpatterns = [
    # /api/snack_request/month_list/
    path('month_list/', api_views.AcceptedMonthListView.as_view()),
]

router.register('api/snack_request', SnackRequestViewSet)
router.register('api/snack_emotion', SnackEmotionViewSet)
