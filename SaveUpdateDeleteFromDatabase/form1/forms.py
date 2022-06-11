from django import forms
from django.core import validators

def start_with_name(name):
    if(name[0] != 't' and name[0] != 'T'):
        raise forms.ValidationError('The name should start with  [ t / T ]')

def start_with_email(email):
    if(email[0] != 't' and email[0] != 'T' ):
        raise forms.ValidationError('The email should start with  [ t / T ]')

def start_with_password(password):
    if(password[0] != 't' and password[0] != 'T'):
        raise forms.ValidationError('The Password should start with [ t / T ]')

class StudentForm(forms.Form):
    name = forms.CharField(validators=[start_with_name])
    email = forms.EmailField(validators=[start_with_email])
    password = forms.CharField(widget = forms.PasswordInput(), validators=[start_with_password])
    
    
        




        

  
    
