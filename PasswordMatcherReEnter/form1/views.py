from django.shortcuts import render
from . forms import StudentForm
from django.http import HttpResponseRedirect


def myDjangoForm(request):
    if request.method == 'POST':
        fm = StudentForm(request.POST)
        if fm.is_valid():
            print('Form validated...\n')
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password1 = fm.cleaned_data['password1']
            password2 = fm.cleaned_data['password2']
           
            print('Validate Name = ', name)
            print('Validate Email = ', email)
            print('Validate Password1 = ', password1)
            print('Validate Password1 = ', password2)
            
            

            #fm = StudentForm()
            # return render(request, 'form1/clickResponse.html', {'nm': name})
            return HttpResponseRedirect('/validate/success/')
    else:
        fm = StudentForm()  # bounded form data
        print("This came from GET method ")
    return render(request, 'form1/Index.html', {'formDjango': fm})


def RegistrationSuccess(request):
    return render(request, 'form1/clickResponse.html')
# StudentForm(auto_id = True,False,chaini_%s etc)
