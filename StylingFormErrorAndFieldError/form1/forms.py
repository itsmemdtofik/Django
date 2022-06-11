from django.core import validators
from django import forms




def start_with_name(name):
    if name[0] != 't':
        raise forms.ValidationError('The name should start with t')

def start_with_email(email):
    if email[0] != 't':
        raise forms.ValidationError('The email should start with t')


class StudentForm(forms.Form):
    error_css_class = 'error'
    required_css_class = 'required'
    name = forms.CharField(validators = [start_with_name])
    email = forms.EmailField(validators = [start_with_email])
    password1 = forms.CharField(widget = forms.PasswordInput())
    password2 = forms.CharField(widget = forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        Password1Validation = self.cleaned_data['password1']
        Password2Validation = self.cleaned_data['password2']
        if Password1Validation != Password2Validation:
            raise forms.ValidationError('Password does not matched ...Please re-enter the password')
        




        

  
    
