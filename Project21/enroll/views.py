from django.shortcuts import render
from enroll.models import Student


def studentinfo(request):
    stud = Student.objects.all()
    print('My Ouptut', stud)
    return render(request, 'enroll/studentDetails.html', {'stu': stud})
