from django.contrib import admin
from .models import Student,Course,Instructor,Subject,Schedule
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Subject)
admin.site.register(Schedule)

# Register your models here.
