from django.shortcuts import render
from django.http import HttpResponse

def courses(request):
    return HttpResponse('welcome to the courses page')
def courses1(request):
    return HttpResponse('review your courses')
def courses2(request):
    return HttpResponse('hi')
# Create your views here.