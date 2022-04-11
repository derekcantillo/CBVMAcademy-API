from django.urls import path 
from .views import StudentView, TeacherView, GroupView, CourseView
urlpatterns = [
   path("students/", StudentView.as_view(), name="student_list"),
   path("students/<int:id>", StudentView.as_view(), name="student_process"),
   path("teachers/", TeacherView.as_view(), name="teacher_list"),
   path("teachers/<int:id>", TeacherView.as_view(), name="teacher_process"),
   path("groups/", GroupView.as_view(), name="group_list"),
   path("groups/<int:id>", GroupView.as_view(), name="group_process"),
   path("courses/", CourseView.as_view(), name="course_list"),
   path("courses/<int:id>", CourseView.as_view(), name="course_process"),
   path("promos/", CourseView.as_view(), name="promo_list"),
   path("promos/<int:id>", CourseView.as_view(), name="promo_process")

]
