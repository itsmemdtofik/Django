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
            price = fm.cleaned_data['price']
            rate = fm.cleaned_data['rate']
            myComment = fm.cleaned_data['myComment']
            myEmail = fm.cleaned_data['myEmail']
            website = fm.cleaned_data['website']
            description = fm.cleaned_data['description']
            feedback = fm.cleaned_data['feedback']
            notes = fm.cleaned_data['notes']
            agree = fm.cleaned_data['agree']

            print('Clead ID = ', ID)
            print('Cleaned Name = ', name)
            print('Cleaned Address = ', address)
            print('Cleaned Contact = ', contact)
            print('Cleaned Email = ', email)
            print('Cleaned Password = ', password)
            print('Cleaned comments = ', comments)
            print('Cleaned price = ', price)
            print('Cleaned rate = ', rate)
            print('Cleaned myComment = ', myComment)
            print('Cleaned myEmail = ', myEmail)
            print('Cleaned website = ', website)
            print('Cleaned description = ', description)
            print('Cleaned feedback = ', feedback)
            print('Cleaned notes = ', notes)
            print('cleaned agree = ', agree)

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
