from django.urls import path
from . import views

urlpatterns = [
   path('registrations/', views.registrations,name='registrations'),
   path('registrations1/', views.registrations1,name='registrations'),
   path('registrations2', views.registrations2,name='registrations'),
   
]
