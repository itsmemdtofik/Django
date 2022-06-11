from django.shortcuts import render
from . forms import StudentForm

def myDjangoForm(request):
	fm = StudentForm()
	return render(request, 'form1/Index.html', {'formDjango':fm})
