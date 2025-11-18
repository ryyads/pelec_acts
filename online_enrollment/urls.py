from django.urls import path
from . import views

urlpatterns = [
 path('online_enrollment/', views.online_enrollment,name='online_enrollment'),
 path('student/', views.student_list,name='student_list'),
 path('course/', views.course_list,name='course_list'),
 path('instructor/', views.instructor_list,name='instructor_list'),
 path('schedule/', views.schedule_list,name='schedule_list'),
 path('subject/', views.subject_list,name='subject_list'),
 path('base/', views.base,name='base'),
 path('enroll/',views.enroll_student, name='enroll_student'),
 path('add_inst/',views.register_instructor, name='register_instructor'),
 path('register/',views.register_user, name='register_user'),
 path('login/',views.login, name='login'),
 path('logout/',views.logout_user, name='logout'),
 path('dashboard/',views.dashboard, name='dashboard'),

 ]
