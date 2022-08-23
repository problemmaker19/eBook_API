from rest_framework import serializers

from eBook.models.mark import Mark
from eBook.serializers.discipline import LessonSerializer
from eBook.serializers.student import StudentSerializer


class MarkSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer()
    student = StudentSerializer()

    class Meta:
        model = Mark
        fields = '__all__'
