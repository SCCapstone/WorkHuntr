from django.contrib.auth.decorators import login_required
from django.core.exceptions import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import *
from users.forms import CodeForm
from .forms import UserLoginForm

def user_login(request):
    logout(request)
    username = password = ''
    if request.method == 'POST':
        context = {}
        context['form'] = UserLoginForm()
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')
        if remember_me:
            request.session.set_expiry(60*60*24*7)  # Set a cookie time to a week
        else:
            request.session.set_expiry(60*60*2)  # set cookie time to a default of 2 hours
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                request.session['pk'] = user.pk
                return redirect('verify')
    else:
        context = {}
        context['form'] = UserLoginForm()
    return render(request, 'users/login.html', context)

def verify(request):
    form = CodeForm(request.POST or None)
    pk = request.session.get('pk')
    if pk:
        user = User.objects.get(pk=pk)
        code = user.code
        code_user = f"{user.username} : {user.code}"
        if not request.POST:
            send_mail(
                subject='Two-Factor Verification Code for WorkHuntr',
                message='Your two-factor verification code for WorkHuntr is ' + str(code) + '.',
                from_email='giantnerds21@gmail.com',
                recipient_list=[user.email],
                fail_silently=False
            )
        if form.is_valid():
            num = form.cleaned_data.get('number')
            if str(code) == num:
                code.save()
                login(request, user)
                return redirect('dashboard')
            else:
                return redirect('login')
    return render(request, 'users/verify.html', {'form' : form})

def home(request):
    return redirect('dashboard')

def dashboard(request):
    return render(request, 'workhuntr/dashboard.html')

def faq(request):
    return render(request, 'workhuntr/faq.html')
