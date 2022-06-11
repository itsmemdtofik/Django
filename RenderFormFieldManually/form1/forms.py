from django import forms

class StudentForm(forms.Form):
	#ID = forms.IntegerField()
	name = forms.CharField(initial='Mohammad Tofik', help_text='You can not write more than thirty character')
	#address = forms.CharField()
	#contact = forms.IntegerField()
	#email = forms.EmailField()
	#passwd = forms.CharField()
	#comment = forms.CharField()