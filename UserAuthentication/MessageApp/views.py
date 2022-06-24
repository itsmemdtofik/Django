from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UserForm
from .models import UserModel
from django.contrib import messages

def UserFun(request):
	messages.info(request,'You can login now to the website')
	messages.success(request,'You can update the page now')
	messages.warning(request,'You can go for Mal Dive Beach ')
	messages.error(request,'I can hit you now ')
	messages.debug(request, 'Helle Debug How are you')
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			reg = UserModel(name = name, email = email, password = password)
			reg.save()
			#messages.add_message(request, messages.INFO, 'Your Account Has Been created !!!')
			#messages.add_message(request, messages.success, 'Your Account Has Been created !!!')
			#messages.success(request, 'Your Account has been succesfully created !!!')
			#messages.info(request, 'Now you can login to the website')
			#print(messages.get_level(request))
			#messages.set_level(request, messages.DEBUG)
			#messages.debug(request, 'This is new debug')
			#print(messages.get_level(request))
			
			

	else:
		form = UserForm()
		print('This came from GET method')
	return render(request, 'MessageApp/User.html', {'form':form})


def SuccessFun(request):
	return render(request, 'MessageApp/Success.html')
