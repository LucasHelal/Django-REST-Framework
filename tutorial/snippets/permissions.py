from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Pernissão personalizada para que apenas donos dos objetos possam edita-ló."""

    def has_object_permission(self, request, view, obj):
        # Leitura, são permitidos a qlqr requisição
        # Assim sempre serão permitidos solicitações de GET, HEAD ou OPTIONS.

        if request.method in permissions.SAFE_METHODS:
            return True

        # As permições de escrita são apenas permitidas penos donos do snippets
        return obj.owner == request.user
