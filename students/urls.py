from django.urls import path
from . import views

urlpatterns = [
 path('students/', views.students, name='students'),
 path('students1/', views.students1, name='students'),
 path('students2/', views.students2, name='students'),
]
