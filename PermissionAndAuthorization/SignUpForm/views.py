from django.shortcuts import render, HttpResponseRedirect
from .forms import SignupForm, EditUserProfile
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User, Group
# Signup Form


def Signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account Created Successfully !!!')
            user = form.save()
            group = Group.objects.get(name = 'editor')
            user.groups.add(group)
    else:
        form = SignupForm()
        print('This came form GET Method')
    return render(request, 'SignUpForm/Signup.html', {'form': form})


#Login
def Login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            print('This came from POST method')
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                passwd = form.cleaned_data['password']
                user = authenticate(username=uname, password=passwd)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logined Successfully !!!')
                    return HttpResponseRedirect('/permissionauthorization/dashboard/')
        else:
            print('This came from GET Method')
            form = AuthenticationForm()
        return render(request, 'SignUpForm/Login.html', {'form': form})
    else:
        return HttpResponseRedirect('/permissionauthorization/dashboard/')

# Dashboard
def UserDashboard(request):
    if request.user.is_authenticated:
        messages.success(request, 'You have logout ???')
        return render(request, 'SignUpForm/Dashboard.html', {'name':request.user.username})
    else:
        return HttpResponseRedirect('/permissionauthorization/login')


# Logout Form


def Logout(request):
    logout(request)
    return HttpResponseRedirect('/permissionauthorization/login/')
