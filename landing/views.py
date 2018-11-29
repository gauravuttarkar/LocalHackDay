from django.shortcuts import render
from .forms import PostForm

# Create your views here.

def home(request):
	return render(request, 'landing/index.html', {})

def login(request):
	return render(request, 'landing/login.html', {})

def signup(request):
	form = PostForm()
	return render(request,'landing/signup.html',{'form':form})