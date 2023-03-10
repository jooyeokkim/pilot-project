from django.db.models import Q
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from utils import date
from .pagination import SnackRequestPagination
from .permissions import IsSnackRequestOwnerOrAdmin
from .serializers import *


class SnackRequestViewSet(mixins.CreateModelMixin,
                          mixins.ListModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          viewsets.GenericViewSet):
    queryset = SnackRequest.objects.all()
    serializer_class = SnackRequestSerializer
    pagination_class = SnackRequestPagination

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'monthly_snack_list', 'legacy_list']:
            self.permission_classes = []
        elif self.action in ['partial_update', 'destroy']:
            self.permission_classes = [IsSnackRequestOwnerOrAdmin]
        elif self.action in ['manage']:
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if request.data.get('is_accepted') == 'off':
            instance.supply_year = None
            instance.supply_month = None
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    # /api/snack_request/legacy_list/
    @action(detail=False, pagination_class=SnackRequestPagination)
    def legacy_list(self, request):
        year, month = date.get_month_list()[0] # 2022, 9
        legacy_qs = self.queryset.filter(Q(supply_year__lt=year)|Q(supply_year=year, supply_month__lt=month))
        queryset = self.filter_queryset(legacy_qs)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # /api/snack_request/52/manage/
    @action(methods=['patch'], detail=True, serializer_class=SnackRequestManageSerializer)
    def manage(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    # /api/snack_request/monthly_list/2023/3/
    @action(url_path=r"monthly_list/(?P<year>\w+)/(?P<month>\w+)", detail=False)
    def monthly_snack_list(self, request, year, month):
        qs = self.queryset.filter(supply_year__exact=year, supply_month__exact=month)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    # /api/snack_request/enroll/
    @action(methods=['post'], detail=False, serializer_class=SnackRequestEnrollSerializer)
    def enroll(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        snack = Snack.objects.get(id=request.data.get('snack'))
        serializer.save(user=request.user, snack=snack)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # /api/snack_request/new_enroll/
    @action(methods=['post'], detail=False, serializer_class=SnackRequestNewEnrollSerializer)
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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class AcceptedMonthListView(APIView):

    # /api/snack_request/month_list/
    def get(self, request):
        return Response({"month_list": date.get_month_list()})
