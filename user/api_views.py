from rest_framework import generics, viewsets, mixins, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .models import User
from .serializers import RegisterSerializer, LoginSerializer, BaseUserSerializer


class UserViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.all()

    def get_permissions(self):
        if self.action in ['upgrade', 'downgrade']:
            self.permission_classes = [IsAdminUser]
        elif self.action in ['quit']:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action in ['create']:
            return RegisterSerializer
        else:
            return BaseUserSerializer

    # /api/user/9/upgrade/
    @action(detail=True) # 통일할 수 있는 선에서 통일
    def upgrade(self, request, pk):
        user = User.objects.get(pk=pk)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return Response(status=status.HTTP_200_OK)

    # /api/user/9/downgrade/
    @action(detail=True)
    def downgrade(self, request, pk):
        user = User.objects.get(pk=pk)
        user.is_staff = False
        user.is_superuser = False
        user.save()
        return Response(status=status.HTTP_200_OK)

    # /api/user/quit/
    @action(detail=False)
    def quit(self, request): # 사용자 입장에서 제거되는 것이라면 delete!!
        # userId = Token.objects.get(key=request.auth.key).user_id
        # user = User.objects.get(id=userId)
        user = request.user
        user.is_active = False
        user.save()
        return Response(status=status.HTTP_200_OK)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data
        return Response(
            {
                "username": token.user.username,
                "token": token.key,
            },
            status=status.HTTP_200_OK
        )
