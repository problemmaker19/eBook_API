from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q
from django.urls import reverse

from eBook.models.student import StudentGroup
from eBook.models.teacher import Teacher


class Discipline(models.Model):
    subject = models.CharField(max_length=8000)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.subject, self.teacher.user.get_full_name()}'


class Lesson(models.Model):
    group = models.ForeignKey(StudentGroup, on_delete=models.CASCADE, null=True, blank=True)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, null=True, blank=True)
    day = models.DateField(u'Day of the lesson', help_text=u'Day of the lesson')
    start_time = models.TimeField(u'Starting time', help_text=u'Starting time')
    end_time = models.TimeField(u'Final time', help_text=u'Final time')

    def get_absolute_url(self):
        url = reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), args=[self.id])
        return u'<a href="%s">%s</a>' % (url, str(self.discipline.subject))

    @staticmethod
    def check_overlap(fixed_start, fixed_end, new_start, new_end):
        overlap = False
        if new_start == fixed_end or new_end == fixed_start:  # edge case
            overlap = False
        elif (fixed_start <= new_start <= fixed_end) or (
                fixed_start <= new_end <= fixed_end):  # innner limits
            overlap = True
        elif new_start <= fixed_start and new_end >= fixed_end:  # outter limits
            overlap = True

        return overlap

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None, *args, **kwargs
    ):
        if self.end_time <= self.start_time:
            raise ValidationError('Ending times must after starting times')
        lessons = Lesson.objects.filter(Q(day=self.day) & Q(group=self.group)).exclude(pk=self.pk)
        if lessons.exists():
            for event in lessons:
                if self.check_overlap(event.start_time, event.end_time, self.start_time, self.end_time):
                    raise ValidationError(
                        'There is an overlap with another lesson: ' + str(event.day) + ', ' + str(
                            event.start_time) + '-' + str(event.end_time))
        super().save(*args, **kwargs)

    def __str__(self):
        return f'''{self.group, self.discipline, 
            self.day.isoformat(), self.start_time.isoformat(), self.end_time.isoformat()}'''


