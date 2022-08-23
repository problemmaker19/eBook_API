from rest_framework import serializers

from eBook.models.discipline import Lesson, Discipline
from eBook.serializers.student import StudentGroupSerializer
from eBook.serializers.teacher import TeacherSerializer


class DisciplineSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()

    class Meta:
        model = Discipline
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    group = StudentGroupSerializer()
    discipline = DisciplineSerializer()

    class Meta:
        model = Lesson
        fields = '__all__'
