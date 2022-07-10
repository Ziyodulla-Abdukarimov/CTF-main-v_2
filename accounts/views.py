from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login as authlogin, logout
from more_itertools import first
from .models import CustomUser

# Create your views here.
def login(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST.get('username'),
                                         password=request.POST.get('password'))
        if user != None:
            authlogin(request, user)
            if user.user_type == "1":
                return HttpResponseRedirect(reverse('staff'))
            elif user.user_type == "2":
                return HttpResponseRedirect(reverse("staffq"))
            else:
                return HttpResponseRedirect(reverse("hacking"))
        else:
            a = messages.error(request, "Foydalanuvchi nomi yoki Parol xato")
    return render(request, 'login/login.html')

def clientadd(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            try:
                user = CustomUser.objects.create_user(first_name=first_name,
                                            last_name=last_name,
                                            email=email,
                                            username=username,
                                            password=password1,
                                            user_type=3
                                            )
                user.save()
                return redirect('login')
            except:
                messages.success(request, 'Bu nomli Foyadalnuvchi bor')
        else:
            messages.success(request, 'Parol tasdiqdan o\'tmadi')
    return render(request,'accounts/register.html')

def log_out(request):
    logout(request)
    return redirect('login')
