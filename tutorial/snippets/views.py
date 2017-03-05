from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from django.contrib.auth.models import User
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework import permissions, reverse, renderers, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, detail_route


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippets-list', request=request, format=format),
    })


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """Este viewset forncece automaticamente ações de 'list' e 'detail'."""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    """
    Este viewset fornece automaticamente ações de 'list', 'create', 'retrive',
    'update' e 'destroy'.
    """

    queryset = Snippet.objects.all()
    serializers_class = SnippetSerializer
    permissions_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class SnippetHighlight(generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     renderer_classes = (renderers.StaticHTMLRenderer,)
#
#     def get(self, request, *args, **kwargs):
#         snippet = self.get_object()
#         return Response(snippet.highlighted)
#
# class SnippetList(generics.ListCreateAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permissions_classes = (permissions.IsAuthenticatedOrReadOnly,)
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#
#
# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permissions_classes = (
#         permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
