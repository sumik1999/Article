from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework import permissions, authentication

# Create your views here.

from .models import User
from .serializers import UserSerializer, AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework import generics


class CreateTokenView(ObtainAuthToken):
    """A view to generate token on providing username and password"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class CreateUserView(generics.CreateAPIView):
    """A view to create an user """
    authentication_classes = []
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()


class ListUserView(generics.ListAPIView):
    """A view to list all users"""
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class DeleteUpdateRetrieveUserView(generics.RetrieveUpdateDestroyAPIView):
    """A view to delete, update and retrieve an user based on id"""
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()
