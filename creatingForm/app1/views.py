from django.shortcuts import render
from app1.forms import RegForm, CommentForm, geekForm


def studentinfo(request):
    #context = {}
    stud = RegForm()
    #context['stud'] = stud
    return render(request, 'app1/home.html', {'form': stud})


def studentComment(request):
    comm = CommentForm()
    return render(request, 'app1/comment.html', {'form1': comm})

def myGeekForm(request):
    geek = geekForm()
    return render(request, 'app1/geek.html', {'form2':geek})
