from django.shortcuts import render
from . forms import StudentForm

def myDjangoForm(request):
	fm = StudentForm(auto_id=True, label_suffix=':', initial={'name':'tofik'})
	return render(request, 'form1/Index.html', {'formDjango':fm})


#StudentForm(auto_id = True,False,chaini_%s etc)