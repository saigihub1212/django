from django.urls import path
from . import views
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import StudentListCreate,TeacherListCreate,CourseListCreate,CreateCourseAPI
urlpatterns = [
    # path('students/',views.get_students),
    # path('students/<int:student_id>/',views.get_student_id),
    # path('course/',views.get_course),
    # path('create/',views.create_student),
    # path('<int:student_id>/',views.update_student),
    # path('<int:student_id>/delete/',views.delete_id)
    path('createCourse/', CreateCourseAPI.as_view()),
    path('tokens/', TokenObtainPairView.as_view()),
    path('tokens/refresh/', TokenRefreshView.as_view()),
    path('students/',StudentListCreate.as_view()),
    path('students/<int:student_id>/',StudentListCreate.as_view()),
    path('teachers/',TeacherListCreate.as_view()),
    path('teachers/<int:teacher_id>/',TeacherListCreate.as_view()),
    path('course/',CourseListCreate.as_view()),
    path('course/<int:course_id>/',CourseListCreate.as_view())
]