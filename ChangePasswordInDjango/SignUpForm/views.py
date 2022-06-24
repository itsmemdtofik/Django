from django.shortcuts import render, HttpResponseRedirect
#from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

#Signup Form
def Signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Account has been created successfully !!!')
	else:
		form = SignupForm()
		print('This came form GET Method')
	return render(request, 'SignUpForm/Signup.html', {'form':form})

"""
def Signup(request):
	if request.method == 'POST':
		form = UserCreationForm()
		if form.is_valid():
			form.save()
			messages.success(request, 'Account has been created successfully !!!')
	else:
		print('This came from GET method !')
		form = UserCreationForm()
	return render(request, 'SignUpForm/Signup.html', {'form':form})
"""

#Login Form
def Login(request):
	if not request.user.is_authenticated:	
		if request.method == 'POST':
			print('This came from POST method')
			form = AuthenticationForm(request = request, data = request.POST)
			if form.is_valid():
				uname = form.cleaned_data['username']
				passwd = form.cleaned_data['password']
				user = authenticate(username = uname, password = passwd)
				if user is not None:
					login(request, user)
					messages.success(request, 'Logined Successfully !!!')
					return HttpResponseRedirect('/user/profile/')
		else:
			print('This came from GET Method')
			form = AuthenticationForm()
		return render(request, 'SignUpForm/Login.html', {'form':form})
	else:
		return HttpResponseRedirect('/user/profile/')


#Profile
def UserProfile(request):
	if request.user.is_authenticated:
	    return render(request, 'SignUpForm/Profile.html', {'name':request.user})
	else:
		return HttpResponseRedirect('/user/login/')

#Logout Form
def Logout(request):
	logout(request)
	return HttpResponseRedirect('/user/login/')

#Change Password with old password
def ChangePasswd(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			form = PasswordChangeForm(user = request.user, data = request.POST)
			if form.is_valid():
				form.save()
				update_session_auth_hash(request, form.user)
				messages.success(request, 'Password Changed Successfully')
				return HttpResponseRedirect('/user/profile/')
		else:
		    form = PasswordChangeForm(user = request.user)
		return render(request, 'SignUpForm/ChangePassword.html', {'form':form})
	else:
		return HttpResponseRedirect('/user/login/')

#Change Password without old password
def ChangePasswd1(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			form = SetPasswordForm(user = request.user, data = request.POST)
			if form.is_valid():
				form.save()
				update_session_auth_hash(request, form.user)
				messages.success(request, 'Password Changed Successfully')
				return HttpResponseRedirect('/user/profile/')
		else:
		    form = SetPasswordForm(user = request.user)
		return render(request, 'SignUpForm/ChangePassword.html', {'form':form})
	else:
		return HttpResponseRedirect('/user/login/')