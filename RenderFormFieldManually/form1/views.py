from django.shortcuts import render
from . forms import StudentForm

def myDjangoForm(request):
	fm = StudentForm(auto_id=True, label_suffix=':')
	fm.order_fields(field_order=['email','passwd','comment','ID','name','contact','address'])
	return render(request, 'form1/Index.html', {'formDjango':fm})


#StudentForm(auto_id = True,False,chaini_%s etc)