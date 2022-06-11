from django.shortcuts import render


def home(request, saal):
    return render(request, 'form1/Index.html' , {'s':saal})

