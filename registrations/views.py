from django.shortcuts import render
from django.http import HttpResponse

def registrations(request):
    return HttpResponse('welcome to the regiostation')
def registrations1(request):
    return HttpResponse('hi')
def registrations2(request):
    return HttpResponse('register now')

# Create your views here.
