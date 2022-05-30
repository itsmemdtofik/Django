from django import forms

class StudentRegistration(forms.Form):
    stuName = forms.CharField()
    stuEmail = forms.EmailField()
    stuPass = forms.CharField()
    