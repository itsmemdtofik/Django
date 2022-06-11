from cProfile import label
from django import forms
from numpy import place


class StudentForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        ValidationName = self.cleaned_data['name']
        ValidationEmail = self.cleaned_data['email']
        ValidationPassword = self.cleaned_data['password']
        if len(ValidationName) < 5 :
            raise forms.ValidationError('Name should be more than 5 characters')
        

        if len(ValidationEmail) < 10 :
            raise forms.ValidationError('Email should be more than 10 characters')
        

        if len(ValidationPassword) < 5 :
            raise forms.ValidationError('Password should be larger than 5 charcters')
        

  
    
