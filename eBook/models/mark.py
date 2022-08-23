from django.core.exceptions import ValidationError
from django.db import models, router

from eBook.models.discipline import Lesson
from eBook.models.student import Student


class Mark(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    points = models.IntegerField(null=True)

    def save(self, force_update=False, update_fields=None, force_insert=False, using=None, *args, **kwargs):
        if not self.lesson.group_id == self.student.group_id:
            raise ValidationError(
                "Student not in mark's lesson group")
        super().save(*args, **kwargs)

    class Meta:
        unique_together = ('student', 'lesson')

    def __str__(self):
        return f'{self.student, self.lesson, self.points}'
