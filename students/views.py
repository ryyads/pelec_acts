from django.shortcuts import render
from rest_framework import viewsets
from .models import Inventory
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset=Inventory.objects.all()
    serializer_class=StudentSerializer


    
# Create your views here.
