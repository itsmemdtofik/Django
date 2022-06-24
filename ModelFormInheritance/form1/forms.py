from dataclasses import fields
from pyexpat import model
from django import forms
from .models import User


class StudentForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['student_name', 'email', 'password']
        #fields = '__all__'
        #exclude = ['teacher_name']
        labels = {'student_name':'','teacher_name':'', 'email':'','password':''}
        #help_text = {'Enter ':'Enter your full name', 'email':'Enter your full email', 'password':'Enter your full password'}
        error_messages = {
        'student_name': {'required': 'Please Enter Your Name'},
        'teacher_name': {'required': 'Please Enter Your Name'},
        'email': {'required': 'Please Enter your email'},
        'password': {'required': 'Please enter your password'}}

        widgets = {
        'student_name': forms.TextInput(attrs={'class': 'myClass', 'placeholder': 'Enter Your Name'}),
        'teacher_name': forms.TextInput(attrs={'class': 'myClass', 'placeholder': 'Enter Your Name'}),
        'email':forms.EmailInput(attrs={'placeholder':'Email'}), 
        'password': forms.PasswordInput(attrs={'placeholder': 'Password'})
        }


class TeacherForm(StudentForm):
    class Meta(StudentForm.Meta):
        fields = ['teacher_name', 'email', 'password']
