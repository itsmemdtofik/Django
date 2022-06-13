from django.core import validators
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ['name', 'email', 'password']
		labels = {'name':'', 'email':'', 'password':''}
		widgets = {
		'name':forms.TextInput(attrs = {'class':'form-control','placeholder':'Name'}),
		'email':forms.EmailInput(attrs = {'class':'form-control', 'placeholder':'Email'}),
		'password':forms.PasswordInput(attrs = {'class':'form-control', 'placeholder':'Password'}, render_value = True)
		}