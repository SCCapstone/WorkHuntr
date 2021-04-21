from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import *
from dms.services import MessagingService
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
            request.session.set_expiry(60*60*24*7)
        else:
            request.session.set_expiry(60*60*2)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                request.session['pk'] = user.pk
                return redirect('verify')
        else:
            messages.error(request, f'An account with that username and password does not exist!')
    else:
        context = {}
        context['form'] = UserLoginForm()
    return render(request, 'users/login.html', context)

def verify(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    form = CodeForm(request.POST or None)
    pk = request.session.get('pk')
    if pk:
        user = User.objects.get(pk=pk)
        code = user.code
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
                messages.error(request, f'Invalid 2FA Key!')
                return redirect('login')
    return render(request, 'users/verify.html', {'form' : form})

def home(request):
    return redirect('dashboard')

def dashboard(request):
    if request.user.is_authenticated:
        unread_messages = MessagingService.get_unread_messages(request, request.user)
        has_unread_messages = True
        num_of_unread_messages = unread_messages.count()
        if not unread_messages:
            has_unread_messages = False
        return render(request, 'workhuntr/dashboard.html', {'has_unread_messages': has_unread_messages, 'num_of_unread_messages': num_of_unread_messages})
    else:
        return render(request, 'workhuntr/dashboard.html')

def faq(request):
    if request.user.is_authenticated:
        unread_messages = MessagingService.get_unread_messages(request, request.user)
        has_unread_messages = True
        num_of_unread_messages = unread_messages.count()
        if not unread_messages:
            has_unread_messages = False
        return render(request, 'workhuntr/faq.html', {'has_unread_messages': has_unread_messages, 'num_of_unread_messages': num_of_unread_messages})
    else:
        return render(request, 'workhuntr/faq.html')
    
def about(request):
    return render(request, 'workhuntr/about.html')    
