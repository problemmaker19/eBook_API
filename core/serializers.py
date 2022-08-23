from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings

from core.models import CustomUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'email', 'is_teacher']
        read_only_field = ['is_active', 'created', 'updated']


class LoginSerializer(TokenObtainPairSerializer):

    def get_token(self, user):
        token = super().get_token(user)
        token['first_name'] = user.first_name
        token['is_teacher'] = user.is_teacher

        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data
