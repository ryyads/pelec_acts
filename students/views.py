from django.shortcuts import render
from django.http import HttpResponse

def students(request):
    return HttpResponse('welcome to the students list')
def students1(request):
    return HttpResponse('raeven maranan')
def students2(request):
    return HttpResponse('report')
# Create your views here.
