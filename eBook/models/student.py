from django.db import models

from core.models import CustomUser


class StudentGroup(models.Model):
    name = models.CharField(max_length=8000)
    year = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.name, self.year}'


class Student(models.Model):
    group = models.ForeignKey(StudentGroup, on_delete=models.CASCADE, null=True, blank=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.user.get_full_name(), self.group}'
