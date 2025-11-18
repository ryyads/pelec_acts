from django import forms 
from .models import Student,Instructor
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class StudentForm(forms.ModelForm):
    class Meta:
        model= Student
        fields =['name','email','date_birth','address','student_id']
    
    def clean_email(self):
        email=self.cleaned_data.get('email')
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError('email must be a gmail address')
        return email
    
class InstructorForm(forms.ModelForm):
    class Meta:
        model= Instructor
        fields =['name','email','phone_number','department','instructor_id']

    def clean_email(self):
        email=self.cleaned_data.get('email')
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError('email must be a gmail address')
        return email
    
class RegisterForm(UserCreationForm):
    email=forms.EmailField(required=True, help_text='Required. Enter a valid email address ')

    class meta:
        model=User
        fields= ['username','email','password1','password2']
