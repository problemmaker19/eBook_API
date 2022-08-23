from rest_framework import serializers

from core.serializers import UserSerializer
from eBook.models.student import StudentGroup, Student


class StudentGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentGroup
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    group = StudentGroupSerializer()
    user = UserSerializer()

    class Meta:
        model = Student
        fields = '__all__'
