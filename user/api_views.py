from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from .models import User
from .serializers import RegisterSerializer, LoginSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


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



class QuitView(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self, request):
        userId = Token.objects.get(key=request.auth.key).user_id
        user = User.objects.get(id=userId)
        user.is_active = False
        user.save()
        return Response(status=status.HTTP_200_OK)


class UpgradeAuthorityView(APIView):
    permission_classes = [IsAdminUser,]

    def post(self, request, pk):
        user = User.objects.get(pk=pk)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return Response(status=status.HTTP_200_OK)


class DowngradeAuthorityView(APIView):
    permission_classes = [IsAdminUser,]

    def post(self, request, pk):
        user = User.objects.get(pk=pk)
        user.is_staff = False
        user.is_superuser = False
        user.save()
        return Response(status=status.HTTP_200_OK)
