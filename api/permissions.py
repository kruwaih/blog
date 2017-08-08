from rest_framework.permissions import BasePermission
from django.utils import timezone
# from posts.model import Post

class AuthorOrStaff(BasePermission):
    message = 'You Must Be The Author'

    def has_object_permission(self, request, view, obj):
        today = timezone.now().date()
        # if request.user.is_staff or request.user.is_superuser or (obj.author == request.user):
        #     return True
        if obj.publish >timezone.now().date() or obj.draft:
            if not (request.user.is_staff or request.user.is_superuser or (obj.author == request.user)):
                return False
        return True
