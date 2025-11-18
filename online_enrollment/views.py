from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Schedule,Student,Subject,Instructor,Course
from .forms import StudentForm,InstructorForm,RegisterForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def online_enrollment(request):
    return HttpResponse('welcome')

def student_list(request):
    student=Student.objects.all()
    
    return render(request, 'student_list.html',{'student':student})
def subject_list(request):
    subject=Subject.objects.all()
    
    return render(request, 'subject_list.html',{'subject':subject})
def course_list(request):
    course=Course.objects.all()
    
    return render(request, 'course_list.html',{'course':course})

def instructor_list(request):
    instructor=Instructor.objects.all()
    
    return render(request, 'instructor_list.html',{'instructor':instructor})

def schedule_list(request):
    schedule=Schedule.objects.all()
    
    return render(request, 'schedule_list.html',{'schedule':schedule})


def base(request):
    student=Student.objects.all()
    subject=Subject.objects.all()
    course=Course.objects.all()
    instructor=Instructor.objects.all()
    schedule=Schedule.objects.all()

    bases={
        'student':student,
        'subject':subject,
        'course':course,
        'instructor':instructor,
        'schedule':schedule

    }
    return render(request, 'base.html',bases)

def enroll_student(request):
    if request.method =='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'students/success.html')
    else:
        form=StudentForm()
    return render(request, 'students/enroll.html',{'form':form})

def register_instructor(request):
    if request.method =='POST':
        form=InstructorForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'instructors/success.html')
    else:
        form=InstructorForm()
    return render(request, 'instructors/register.html',{'form':form})

def register_user(request):
    if request.method =='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'account created successfully! you can now log in')
            return render(request,'login_user')
    else:
        form=RegisterForm()
    return render(request, 'accounts/register.html',{'form':form})

def login(request):
    if request.method =='POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request, user)               
                messages.success(request, f'welcom back,{username}')
                return render(request,'dashboard')
            else:
                messages.error(request,'invalid username or passsword')
        else:
                messages.error(request,'invalid imput')
    else:
        form=AuthenticationForm()
    return render(request, 'accounts/login.html',{'form':form})

def logout_user(request):
    logout(request)
    messages.info(request, 'you have been logout')
    return redirect ('login_user')

def dashboard(request):
    return render(request,'accounts/dashboard.html')
    







