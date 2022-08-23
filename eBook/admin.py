import calendar
from datetime import timedelta
from django.conf import settings
import datetime
from django.contrib import admin
from django.db.models import Q
from django.urls import reverse
from django.utils.safestring import mark_safe

from eBook.calendar import EventCalendar
from eBook.models.discipline import Discipline, Lesson
from eBook.models.mark import Mark
from eBook.models.student import Student, StudentGroup
from eBook.models.teacher import Teacher

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(StudentGroup)
admin.site.register(Discipline)


@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ['lesson', 'student', 'points']


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['group', 'discipline', 'day', 'start_time', 'end_time']
    list_filter = ['group', 'day', 'discipline']
    actions = ['fill_semester', 'clear_semester']
    change_list_template = 'admin/lesson/change_list.html'

    def changelist_view(self, request, extra_context=None):
        after_day = request.GET.get('day__gte', None)
        extra_context = extra_context or {}

        if not after_day:
            d = datetime.date.today()
        else:
            try:
                split_after_day = after_day.split('-')
                d = datetime.date(year=int(split_after_day[0]), month=int(split_after_day[1]), day=1)
            except:
                d = datetime.date.today()

        previous_month = datetime.date(year=d.year, month=d.month, day=1)  # find first day of current month
        previous_month = previous_month - datetime.timedelta(days=1)  # backs up a single day
        previous_month = datetime.date(year=previous_month.year, month=previous_month.month,
                                       day=1)  # find first day of previous month

        last_day = calendar.monthrange(d.year, d.month)
        next_month = datetime.date(year=d.year, month=d.month, day=last_day[1])  # find last day of current month
        next_month = next_month + datetime.timedelta(days=1)  # forward a single day
        next_month = datetime.date(year=next_month.year, month=next_month.month,
                                   day=1)  # find first day of next month

        extra_context['previous_month'] = reverse('admin:eBook_lesson_changelist') + '?day__gte=' + str(
            previous_month)
        extra_context['next_month'] = reverse('admin:eBook_lesson_changelist') + '?day__gte=' + str(next_month)

        cal = EventCalendar()
        html_calendar = cal.formatmonth(d.year, d.month, request, withyear=True)
        html_calendar = html_calendar.replace('<td ', '<td  width="100" height="100"')
        extra_context['calendar'] = mark_safe(html_calendar)
        return super(LessonAdmin, self).changelist_view(request, extra_context)

    @admin.action(description='Fill the semester with selected lessons')
    def fill_semester(self, request, queryset):
        delta = timedelta(weeks=1)
        for item in queryset:
            start_date = settings.SEMESTER_BEGIN
            end_date = settings.SEMESTER_END
            if start_date <= item.day <= end_date:
                item.delete()
            if start_date.isoweekday() > item.day.isoweekday():
                start_date += timedelta(days=7 - (start_date.isoweekday() - item.day.isoweekday()))
            elif start_date.isoweekday() < item.day.isoweekday():
                start_date += timedelta(days=item.day.isoweekday() - start_date.isoweekday())
            while start_date <= end_date:
                item.id = None
                item.day = start_date
                item.save()
                start_date += delta

    @admin.action(description='Clear semester of selected lessons')
    def clear_semester(self, request, queryset):
        start_date = settings.SEMESTER_BEGIN
        end_date = settings.SEMESTER_END
        for item in queryset:
            Lesson.objects.filter(day__range=[start_date, end_date]) \
                .filter(Q(group=item.group) & Q(discipline=item.discipline) &
                        Q(start_time=item.start_time) & Q(end_time=item.end_time) &
                        Q(day__week_day=item.day.isoweekday() % 7 + 1)).delete()

