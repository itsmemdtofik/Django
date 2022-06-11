from django.shortcuts import render
from . forms import StudentForm
from django.http import HttpResponseRedirect
from .models import StudentRegistration

def myDjangoForm(request):
    if request.method == 'POST':
        fm = StudentForm(request.POST)
        if fm.is_valid():
            print('Form validated...\n')
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            #registraion = StudentRegistration(name = name, email = email, password = password) #This line is for insert into the database
            #registration = StudentRegistration(id = 1, name = name, email = email, password = password) #This line is for update the database
            #registration.save() #The save function have two properties one is can insert the database and also can update to the database
            regitration = StudentRegistration(id = 2) #This line is for deleting the database for particular data
            regitration.delete() #The delete function delete the database
            #fm = StudentForm()
            # return render(request, 'form1/clickResponse.html', {'nm': name})
            return HttpResponseRedirect('/database/success/')
    else:
        fm = StudentForm()  # bounded form data
        print("This came from GET method ")
    return render(request, 'form1/Index.html', {'formDjango': fm})


def RegistrationSuccess(request):
    return render(request, 'form1/clickResponse.html')
# StudentForm(auto_id = True,False,chaini_%s etc)
