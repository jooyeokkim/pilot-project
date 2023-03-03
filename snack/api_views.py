from rest_framework import viewsets, mixins, permissions, generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, action
from rest_framework import generics

from utils import date
from .models import Snack
from .pagination import SnackPagination
from .serializers import SnackSerializer


class SnackViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):

    queryset = Snack.objects.all()
    serializer_class = SnackSerializer
    pagination_class = SnackPagination

    def get_permissions(self):
        if self.request.method=='GET':
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated,]
        return [permission() for permission in permission_classes]

    # /api/snack/accepted_snack_list/
    @action(detail=False, permission_classes=[])
    def accepted_snack_list(self, request):
        qs = self.queryset.filter(is_accepted=True)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    # /api/snack/monthly_list/2023/3/
    @action(detail=False, url_path=r"monthly_list/(?P<year>\w+)/(?P<month>\w+)")
    def monthly_snack_list(self, request, year, month):
        qs = self.queryset.filter(supply_year__exact=year, supply_month__exact=month)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)


class AcceptedMonthListView(APIView):

    # /api/snack/month_list/
    def get(self, request):
        return Response({"month_list": date.get_month_list(self)})