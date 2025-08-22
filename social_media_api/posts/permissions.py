from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Read: everyone; Write: only object owner.
    """

    def has_object_permission(self, request, view, obj):
        # SAFE: GET/HEAD/OPTIONS allowed for anyone
        if request.method in permissions.SAFE_METHODS:
            return True
        # write ops only if the requesting user is the author/owner
        return getattr(obj, "author_id", None) == getattr(request.user, "id", None)
