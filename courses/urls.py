from django.urls import path
from . import views

urlpatterns = [
 path('courses/', views.courses,name='courses'),
 path('courses1/', views.courses1,name='courses'),
 path('courses2/', views.courses2,name='courses'),
 ]
