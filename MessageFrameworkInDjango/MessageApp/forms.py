from os import fchdir
from django import forms
from .models import UserModel


class UserForm(forms.ModelForm):
	class Meta:
		model = UserModel
		fields = ['name', 'email', 'password']
		labels = {'name':'', 'email':'', 'password':''}
		error_messages = {
		    'name':{'required':'Enter your name'},
		    'email':{'required':'Enter your email'},
		    'password':{'required':'Enter your password'}
		}
		widgets = {
        'name': forms.TextInput(attrs={'placeholder': 'Enter Your Name'}),
        'email':forms.EmailInput(attrs={'placeholder':'Email'}), 
        'password': forms.PasswordInput(attrs={'placeholder': 'Password'})
        }