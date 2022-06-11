from django.shortcuts import render
from . forms import StudentForm
from django.http import HttpResponseRedirect

def myDjangoForm(request):
	if request.method == 'POST':
		fm = StudentForm(request.POST)
		if fm.is_valid():
            
		    ID = fm.cleaned_data['ID']
		    name = fm.cleaned_data['name']
		    address = fm.cleaned_data['address']
		    contact = fm.cleaned_data['contact']
		    email = fm.cleaned_data['email']
		    password = fm.cleaned_data['password']
		    comments = fm.cleaned_data['comments']

		    print('Clead ID = ', ID)
		    print('Cleaned Name = ', name)
		    print('Cleaned Address = ', address)
		    print('Cleaned Contact = ', contact)
		    print('Cleaned Email = ', email)
		    print('Cleaned Password = ', password)
		    print('Cleaned comments = ', comments)
		    #fm = StudentForm()
		    #return render(request, 'form1/clickResponse.html', {'nm': name})
		    return HttpResponseRedirect('/validate/success/')
	else:
		fm = StudentForm() #bounded form data
		print("This came from GET method ")
	return render(request, 'form1/Index.html', {'formDjango':fm})

def RegistrationSuccess(request):
	return render(request, 'form1/clickResponse.html')
#StudentForm(auto_id = True,False,chaini_%s etc)