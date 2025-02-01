from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request,"Başarılı giriş")
            return redirect('home')
        else:
            messages.error(request,"Hatalı giriş")
            return render(request,'login.html')
    return render(request,'login.html')


@login_required 
def home(request):
    return render(request,'dashboard.html')
def logout(request):
    messages.success(request,"Başarılı Çıkış Yapıldı")
    return render(request,'login.html')