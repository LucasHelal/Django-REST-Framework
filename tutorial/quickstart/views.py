from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """API que permite que os usuário sejam visualizados ou editados."""

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """API que permite que os grupos sejam visualizados ou editados."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
