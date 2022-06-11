from cProfile import label
from django import forms
from numpy import place


class StudentForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_name(self):
        validationName = self.cleaned_data['name']
        if len(validationName) < 5:
            raise forms.ValidationError('Please Enter more than 5 charcters')
        return validationName

    def clean_email(self):
        ValidationEmail = self.cleaned_data['email']
        if len(ValidationEmail) < 11:
            raise forms.ValidationError('Please Enter more than 11 characters')
        return ValidationEmail

    def clean_password(self):
        ValidationPassword = self.cleaned_data['password']
        if len(ValidationPassword) < 5:
            raise forms.ValidationError('Please Enter more than 5 Characters')
        return ValidationPassword
  
    
