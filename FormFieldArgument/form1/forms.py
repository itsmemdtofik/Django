from django import forms

class StudentForm(forms.Form):
	ID = forms.IntegerField()
	name = forms.CharField(label = 'Your Name', label_suffix = ' ', initial = 'Mohammad Tofik', required = False, disabled = True, help_text = 'Please do not enter with 30 character')
	address = forms.CharField()
	contact = forms.IntegerField()
	email = forms.EmailField()
	passwd = forms.CharField()
	comment = forms.CharField()
	key = forms.CharField(widget=forms.HiddenInput())