from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from .models import BlogPost

class SignupForm(UserCreationForm):
	password1 = forms.CharField(label = 'Password', widget = forms.PasswordInput(attrs = {'class':'form-control'}))
	password2 = forms.CharField(label = 'Re-Enter Password', widget = forms.PasswordInput(attrs = {'class':'form-control'}))
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email']
		labels = {'first_name':'First Name', 'last_name':'Last Name', 'email':'Email'}

		widgets = {
		'username':forms.TextInput(attrs = {'class':'form-control'}),
		'first_name':forms.TextInput(attrs = {'class':'form-control'}),
		'last_name':forms.TextInput(attrs = {'class':'form-control'}),
		'email':forms.EmailInput(attrs = {'class':'form-control'})
		}

class LoginForm(AuthenticationForm):
	username = UsernameField(widget = forms.TextInput(attrs = {'autofocus':True, 'class':'form-control'}))
	password = forms.CharField(widget = forms.PasswordInput(attrs = {'autocomplete':'current_password', 'class':'form-control'}), label = _("Password"), strip = False)

class PostForm(forms.ModelForm):
	class Meta:
		model = BlogPost
		fields = ['title', 'description']
		labels = {'title':'Title', 'description':'Description'}

		widgets = {
		'title':forms.TextInput(attrs = {'class':'form-control'}),
		'description':forms.Textarea(attrs = {'class':'form-control'})
		}