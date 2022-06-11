from django import forms

class StudentForm(forms.Form):
	ID = forms.IntegerField()
	name = forms.CharField()
	address = forms.CharField(widget = forms.TextInput(attrs={'class':'Address','ID':'Uniqueid'}))
	contact = forms.IntegerField()
	email = forms.EmailField()
	password = forms.CharField(widget = forms.PasswordInput())
	comments = forms.CharField(widget = forms.Textarea())
	