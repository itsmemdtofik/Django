from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SignupForm, LoginForm, PostForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import BlogPost
from django.contrib.auth.models import Group


def home(request):
	posts = BlogPost.objects.all()
	return render(request, 'Blog/Home.html', {'posts': posts})


def about(request):
	return render(request, 'Blog/About.html')


def contact(request):
	return render(request, 'Blog/Contact.html')


def dashboard(request):
	if request.user.is_authenticated:
		posts = BlogPost.objects.all()
		user = request.user
		full_name = user.get_full_name()
		gps = user.groups.all()
		ip = request.session.get('ip', 0)
		return render(request, 'Blog/Dashboard.html', {'posts':posts, 'groups':gps, 'full_name':full_name, 'ip' : ip})
	else:
		HttpResponseRedirect('/login/')


def UserLogout(request):
	logout(request)
	return HttpResponseRedirect('/')

def UserSignup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			messages.success(request, 'Congratulations ! | Your Account Has Been Created Successfully !')
			form.save()
	else:
		form = SignupForm()
	return render(request, 'Blog/Signup.html', {'form':form})

def UserLogin(request):
	if not request.user.is_authenticated:
		if request.method == 'POST':
			form = LoginForm(request = request, data = request.POST)
			if form.is_valid():
				uname = form.cleaned_data['username']
				passwd = form.cleaned_data['password']
				user = authenticate(username = uname, password = passwd)
				messages.success(request, 'You Have Logined Successfully !')
				if user is not None:
					login(request, user)
				return HttpResponseRedirect('/dashboard/')
		else:
			form = LoginForm()
		return render(request, 'Blog/Login.html', {'form':form})
	else:
		return HttpResponseRedirect('/dashboard/')


def AddPost(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			form = PostForm(request.POST)
			if form.is_valid():
				title = form.cleaned_data['title']
				desc = form.cleaned_data['description']
				post = BlogPost(title = title, description = desc)
				post.save()
				messages.success(request, 'Post Added Successfully !')
				form = PostForm()
		else:
			form = PostForm()
		return render(request, 'Blog/Addpost.html', {'form':form})
	else:
		return HttpResponseRedirect('/login/')


def UpdatePost(request, id):
	if request.user.is_authenticated:
		if request.method == 'POST':
			id = BlogPost.objects.get(pk = id)
			form = PostForm(request.POST, instance = id)
			if form.is_valid():
				user = form.save()
				group = Group.objects.get(name = 'Author')
				user.groups.add(group)
		else:
			id = BlogPost.objects.get(pk = id)
			form = PostForm(instance = id)
		return render(request, 'Blog/Updatepost.html', {'form':form})
	else:
		return HttpResponseRedirect('/login/')

def DeletePost(request, id):
	if request.user.is_authenticated:
		if request.method == 'POST':
			id = BlogPost.objects.get(pk = id)
			id.delete()
		return HttpResponseRedirect('/dashboard/')
	else:
		return HttpResponseRedirect('/login/')
