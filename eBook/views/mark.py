from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from eBook.filters import MarkFilter
from eBook.models.mark import Mark
from eBook.permissions import IsTeacher
from eBook.serializers.mark import MarkSerializer


class MarkViewSet(viewsets.ModelViewSet):
    queryset = Mark.objects.all()
    filter_backends = [MarkFilter]
    permission_classes = (IsAuthenticated,)
    serializer_class = MarkSerializer

    def get_permissions(self):
        if self.request.method != 'GET':
            self.permission_classes = [IsTeacher]
        return super(MarkViewSet, self).get_permissions()

