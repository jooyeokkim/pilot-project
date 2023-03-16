from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from utils import date
from .filters import SnackRequestFilter
from .pagination import SnackRequestPagination
from .permissions import IsSnackRequestOwnerOrAdmin
from .serializers import *


class SnackRequestViewSet(mixins.CreateModelMixin,
                          mixins.ListModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          viewsets.GenericViewSet):

    queryset = SnackRequest.objects.order_by_like_proportion()
    pagination_class = SnackRequestPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = SnackRequestFilter

    serializer_class_dict = {
        'list': SnackRequestSerializer,
        'partial_update': SnackRequestEditSerializer,
        'manage': SnackRequestManageSerializer,
        'create': SnackRequestEnrollSerializer,
        'new_enroll': SnackRequestNewEnrollSerializer
    }

    def get_permissions(self):
        if self.action in ['list']:
            self.permission_classes = []
        elif self.action in ['partial_update', 'destroy']:
            self.permission_classes = [IsSnackRequestOwnerOrAdmin]
        elif self.action in ['manage']:
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def get_serializer_class(self):
        return self.serializer_class_dict.get(self.action)

    # /api/snack_request/52/manage/
    @action(methods=['patch'], detail=True)
    def manage(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    # /api/snack_request/new_enroll/
    @action(methods=['post'], detail=False)
    def new_enroll(self, request, *args, **kwargs):
        data = {
            'snack': {
                'name': request.data.get('name'),
                'image': request.data.get('image'),
                'url': request.data.get('url'),
            },
            'description': request.data.get('description')
        }
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class SnackEmotionViewSet(mixins.CreateModelMixin,
                          mixins.ListModelMixin,
                          viewsets.GenericViewSet):
    queryset = SnackEmotion.objects.all()
    serializer_class = SnackEmotionSerializer

    def get_permissions(self):
        if self.action in ['create']:
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = []
        return super().get_permissions()


class AcceptedMonthListView(APIView):

    # /api/snack_request/month_list/
    def get(self, request):
        return Response({"year_month_list": date.get_year_month_list()})
