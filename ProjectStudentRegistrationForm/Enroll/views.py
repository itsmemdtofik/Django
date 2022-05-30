from django.shortcuts import render
from Enroll.forms import StudentRegistration


def studentinfo(request):
    stud = StudentRegistration()
    return render(request, 'Enroll/studentdetails.html', {'form': stud})

# Create your views here.
