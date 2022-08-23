from rest_framework import serializers

from core.serializers import UserSerializer
from eBook.models.teacher import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Teacher
        fields = '__all__'
