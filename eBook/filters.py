from django.db.models import Q
from rest_framework import filters


class MarkFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        queryset = queryset.filter(Q(lesson__discipline__teacher__user_id=request.user.id)
                                   | Q(student_id=request.user.id))
        return queryset
