from django.shortcuts import render
from databaseapp1.models import StudentForm


def studentinfo(request):
    studDetails = StudentForm.objects.all()
    return render(request, 'databaseapp1/index.html', {'form': studDetails})

# Create your views here.
