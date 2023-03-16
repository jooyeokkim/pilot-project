from rest_framework import generics, viewsets, mixins, status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .models import User
from .serializers import RegisterSerializer, LoginSerializer, BaseUserSerializer


class UserViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
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


# 토큰으로 직접 유저 찾기
# userId = Token.objects.get(key=request.auth.key).user_id
# user = User.objects.get(id=userId)

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data
        return Response(
            {
                "id": token.user.id,
                "username": token.user.username,
                "token": token.key,
            },
            status=status.HTTP_200_OK
        )
