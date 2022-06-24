from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class SignupForm(UserCreationForm):
	password1 = forms.CharField(label = '', widget = forms.PasswordInput(attrs = {'placeholder':'Enter Password', 'autocomplete':'off', 'class':'form-control','id':'form'}))
	password2 = forms.CharField(label = '', widget = forms.PasswordInput(attrs = {'placeholder':'Re-Confirm Password', 'autocomplete':'off', 'class':'form-control','id':'form'}))
	class Meta:
		model = User
		fields = ['username', 'first_name','last_name', 'email']
		labels = {'username':'', 'email':'', 'first_name':'', 'last_name':''}
		
		widgets = {
		'username':forms.TextInput(attrs={'placeholder': 'Enter User Name', 'class':'form-control', 'autocomplete':'off','id':'form'}),
        'first_name': forms.TextInput(attrs={'placeholder': 'Enter Your First Name', 'class':'form-control', 'autocomplete':'off','id':'form'}),
        'last_name': forms.TextInput(attrs={'placeholder': 'Enter Yor Last Name', 'class':'form-control', 'autocomplete':'off','id':'form'}),
        'email':forms.EmailInput(attrs={'placeholder':'Enter Your Email', 'class':'form-control', 'autocomplete':'off','id':'form'}), 
        }

class EditUserProfile(UserChangeForm):
	password = None
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login', 'is_active']
		labels = {'email':'Email'}

		widgets = {
		'username':forms.TextInput(attrs={'placeholder': 'Enter User Name', 'class':'form-control', 'autocomplete':'off','id':'form'}),
        'first_name': forms.TextInput(attrs={'placeholder': 'Enter Your First Name', 'class':'form-control', 'autocomplete':'off','id':'form'}),
        'last_name': forms.TextInput(attrs={'placeholder': 'Enter Yor Last Name', 'class':'form-control', 'autocomplete':'off','id':'form'}),
        'email':forms.EmailInput(attrs={'placeholder':'Enter Your Email', 'class':'form-control', 'autocomplete':'off','id':'form'}),
        'date_joined':forms.EmailInput(attrs={'placeholder':'Enter Your Email', 'class':'form-control', 'autocomplete':'off','id':'form'}),
        'last_login':forms.EmailInput(attrs={'placeholder':'Enter Your Email', 'class':'form-control', 'autocomplete':'off','id':'form'}),
        }

