from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.


def h(request):
    return render(request,'hello.html')

def home(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"you Have been sucesfully login")
            return redirect('home')
        else:
            messages.error(request,"invalid username or password")
            return redirect('home')
    else:       
        return render(request,'home.html')

def logout_user(request):
    logout(request)
    messages.success(request,"You Have Been Logout Sucessfully")
    return redirect('home')

