from django.shortcuts import render
#from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm
from django.contrib import messages


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