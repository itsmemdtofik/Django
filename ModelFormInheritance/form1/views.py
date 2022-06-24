from django.shortcuts import render
from . forms import StudentForm, TeacherForm
from django.http import HttpResponseRedirect
from .models import User


def StudentFun(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            print('Form validated...\n')
            student_name = form.cleaned_data['student_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            regitration = User(student_name = student_name, email = email, password = password)
            regitration.save()
            return HttpResponseRedirect('/modelform/success/')
    else:
        form = StudentForm()  # bounded form data
        print("This came from GET method ")
    return render(request, 'form1/Index.html', {'student': form})



def TeacherFun(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            teacher_name = form.cleaned_data['teacher_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            teacherReg = User(teacher_name = teacher_name, email = email, password = password)
            teacherReg.save()
            return HttpResponseRedirect('/modelform/success/')
    else:
        form = TeacherForm()
        print("This came from GET method")
    return render(request, 'form1/teacher.html', {'teacher': form}) 


def RegistrationSuccess(request):
    return render(request, 'form1/clickResponse.html')
# StudentForm(auto_id = True,False,chaini_%s etc)
