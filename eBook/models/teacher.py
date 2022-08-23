from django.db import models

from core.models import CustomUser


class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.user.get_full_name()}'
