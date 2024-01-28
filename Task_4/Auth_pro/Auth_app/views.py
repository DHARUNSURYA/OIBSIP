from django.shortcuts import render,redirect
from .forms import uss
from. models import *
from django.contrib import messages

from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    return render(request,'index.html')

def singup(request):
    form=uss()
    if request.method=='POST':
        form=uss(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('login')
            except:
                pass
        
    return render(request,'register.html',{'form':form})

def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Logged In Successfully...!")
            return redirect('home')
        else:
            messages.error(request, "Invalid Username Or Password..!")
            return render(request, 'login.html')
    
    return render(request, 'login.html')
def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged Out Successfully...!")
        return redirect('/')