from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from stores.models import Category


# Create your views here.
def shop(request):
    return render(request,'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user1 = auth.authenticate(username=username, password=password)
        if user1 is not None:
            auth.login(request, user1)
            return redirect('stores:product')
        else:
            messages.info(request, "invalid details")
            return redirect('stores:login')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken")
                return redirect('stores:register')
            else:
                user1 = User.objects.create_user(username=username, password=password)
                user1.save()
                return redirect('stores:login')


        else:
            messages.info(request, "password not matching")
            return redirect('stores:register')
        # return redirect('/')
    return render(request, "register.html")

def product(request):
    product=Category.objects.all()
    return render(request,'index1.html',{'product':product})
