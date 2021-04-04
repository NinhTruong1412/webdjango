from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm

from .forms import RegisterForm

def register(response):
	if response.method == "POST":
		form = RegisterForm(response.POST)
		if form.is_valid():
			form.save()
			return redirect("/home/")
	else:
		form = RegisterForm()
	return render(response,'register/register.html',{'form':form})


def login(request):
	if request.method == "POST":
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			return redirect("/home/")
	else:
		form = AuthenticationForm()
	return render(request,'register/login.html',{'form':form})

