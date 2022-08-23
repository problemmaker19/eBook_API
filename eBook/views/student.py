from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from eBook.models.student import StudentGroup, Student
from eBook.serializers.student import StudentGroupSerializer, StudentSerializer


class StudentGroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupSerializer
    permission_classes = (IsAuthenticated,)


class StudentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (IsAuthenticated,)
