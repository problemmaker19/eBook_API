from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from eBook.models.teacher import Teacher
from eBook.serializers.teacher import TeacherSerializer


class TeacherViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = (IsAuthenticated,)
