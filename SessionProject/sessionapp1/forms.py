from django import forms

#First we create the form then we validate to it in views.py file
class SessionForm(forms.Form):
	username = forms.CharField(max_length = 100)
	contactNumber = forms.IntegerField()