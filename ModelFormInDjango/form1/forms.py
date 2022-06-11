from dataclasses import fields
from pyexpat import model
from django import forms
from .models import StudentRegistration


class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentRegistration
        fields = ['name', 'email', 'password']
        labels = {'name': '', 'email': '', 'password': ''}
        #help_text = {'Enter ':'Enter your full name', 'email':'Enter your full email', 'password':'Enter your full password'}
        error_messages = {'name': {'required': 'Please Enter Your Name'}, 'email': {
            'required': 'Please Enter your email'}, 'password': {'required': 'Please enter your password'}}
        widgets = {'name': forms.TextInput(attrs={'class': 'myClass', 'placeholder': 'Enter Your Name'}), 'password': forms.PasswordInput(attrs={'placeholder': 'Enter Your Password'})}
