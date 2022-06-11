from django import forms

class StudentForm(forms.Form):
	ID = forms.IntegerField()
	name = forms.CharField()
	address = forms.CharField()
	contact = forms.IntegerField()
	email = forms.EmailField()
	passwd = forms.CharField()
	comment = forms.CharField()