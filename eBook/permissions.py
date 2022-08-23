from django.core.exceptions import ValidationError
from rest_framework.permissions import BasePermission

from eBook.models.discipline import Lesson


class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        if request.user.id != Lesson.objects.get(pk=request.data.get('lesson')).discipline.teacher.user.id:
            raise ValidationError('Access denied')
        return True
