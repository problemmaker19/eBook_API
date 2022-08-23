from api.router import router
from eBook.views.discipline import LessonViewSet, DisciplineViewSet
from eBook.views.mark import MarkViewSet
from eBook.views.student import StudentViewSet, StudentGroupViewSet
from eBook.views.teacher import TeacherViewSet

router.register(r'group', StudentGroupViewSet, basename='group')
router.register(r'student', StudentViewSet, basename='student')
router.register(r'teacher', TeacherViewSet, basename='teacher')
router.register(r'discipline', DisciplineViewSet, basename='discipline')
router.register(r'lesson', LessonViewSet, basename='lesson')
router.register(r'mark', MarkViewSet, basename='mark')


