from cProfile import label
from django import forms
from numpy import place


class StudentForm(forms.Form):
    ID = forms.IntegerField()
    name = forms.CharField(min_length=5, max_length=10, strip=False,
                           empty_value='tofik', error_messages={'required': 'Enter your name '})
    address = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'Address', 'ID': 'Uniqueid'}))
    contact = forms.IntegerField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    comments = forms.CharField(widget=forms.Textarea())
    price = forms.DecimalField(
        min_value=5, max_value=100, max_digits=5, decimal_places=1)
    rate = forms.FloatField(min_value=5, max_value=16)
    myComment = forms.SlugField()
    myEmail = forms.EmailField(min_length=5, max_length=100)
    website = forms.URLField(min_length=5, max_length=100)
    description = forms.CharField(widget=forms.Textarea())
    feedback = forms.CharField(min_length=5, max_length=100, widget=forms.TextInput(
        attrs={'class': 'clascse1 classcse2', 'id': 'uniqueid'}))
    notes = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 3, 'cols': 50}))
    agree = forms.BooleanField(label_suffix='', label='ENter your name ', error_messages={
        'required': 'Enter the correct name'})
