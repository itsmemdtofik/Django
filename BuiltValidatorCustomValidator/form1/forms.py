from django.core import validators
from django import forms



#This is custom form validator
def start_with_name(name):
    if name[0] != 't':
        raise forms.ValidationError('The name should start with t')

def start_with_email(email):
    if email[0] != 't':
        raise forms.ValidationError('The email should start with t')

def start_with_password(password):
    if password[0] != 't':
        raise forms.ValidationError('The password should start with t')

class StudentForm(forms.Form):
    name = forms.CharField(validators = [start_with_name])
    email = forms.EmailField(validators = [start_with_email])
    password = forms.CharField(widget = forms.PasswordInput(), validators = [start_with_password])







#This is built validator
#class StudentForm(forms.Form):
   # name = forms.CharField(validators = [validators.MaxLengthValidator(10)])
    #email = forms.EmailField(validators=[validators.MaxLengthValidator(10)])
    #password = forms.CharField(widget=forms.PasswordInput(), validators=[validators.MaxLengthValidator(10)])
        

  
    
