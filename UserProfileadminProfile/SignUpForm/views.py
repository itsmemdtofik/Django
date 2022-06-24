from django.shortcuts import render, HttpResponseRedirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm, EditUserProfile, EditAdminProfile
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User


#Signup Form
def Signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Account has been created successfully !!!')
    else:
        form = SignupForm()
        print('This came form GET Method')
    return render(request, 'SignUpForm/Signup.html', {'form': form})



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
                    return HttpResponseRedirect('/useradmin/profile/')
        else:
            print('This came from GET Method')
            form = AuthenticationForm()
        return render(request, 'SignUpForm/Login.html', {'form': form})
    else:
        return HttpResponseRedirect('/useradmin/profile/')


# Profile
def UserProfile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_superuser == True:
                form = EditAdminProfile(request.POST, instance = request.user)
                users = User.objects.all()
            else:
                form = EditUserProfile(request.POST, instance = request.user)
                users = None
            if form.is_valid():
                messages.success(request, 'Profile Updated Successfully !!!')
                form.save()
        else:
            if request.user.is_superuser == True:
                form = EditAdminProfile(instance = request.user)
                users = User.objects.all()
            else:
                form = EditUserProfile(instance = request.user)
                users = None
        return render(request, 'SignUpForm/Profile.html',{'name':request.user.username, 'form':form, 'users':users})
    else:
        return HttpResponseRedirect('/useradmin/login')


# Logout Form


def Logout(request):
    logout(request)
    return HttpResponseRedirect('/useradmin/login/')

# Change Password with old password


def ChangePasswd(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, 'Password Changed Successfully !!!')
                return HttpResponseRedirect('/useradmin/profile/')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, 'SignUpForm/ChangePassword.html', {'form': form})
    else:
        return HttpResponseRedirect('/useradmin/login/')


#UserDetails
def UserDetails(request, id):
    if request.user.is_authenticated:
        id = User.objects.get(pk = id)
        form = EditAdminProfile(instance = id)
        return render(request, 'SignUpForm/userdetails.html', {'form':form})
    else:
        return HttpResponseRedirect('/useradmin/login/')
