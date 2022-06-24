from dataclasses import fields
from pyexpat import model
from django import forms
from .models import StudentModel


class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        #exclude = ['name']
        labels = {'name':'', 'email':'','password':''}
        #help_text = {'Enter ':'Enter your full name', 'email':'Enter your full email', 'password':'Enter your full password'}
        error_messages = {'name': {'required': 'Please Enter Your Name'}, 'email': {
            'required': 'Please Enter your email'}, 'password': {'required': 'Please enter your password'}}
        widgets = {'name': forms.TextInput(attrs={'class': 'myClass', 'placeholder': 'Enter Your Name'}),
        'email':forms.EmailInput(attrs={'placeholder':'Email'}), 
        'password': forms.PasswordInput(attrs={'placeholder': 'Password'})
        }
