from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from eBook.models.discipline import Discipline, Lesson
from eBook.serializers.discipline import LessonSerializer, DisciplineSerializer


class DisciplineViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer
    permission_classes = (IsAuthenticated,)


class LessonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated,)
