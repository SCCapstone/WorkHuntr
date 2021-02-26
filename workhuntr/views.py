from django.contrib.auth.decorators import login_required
from django.core.exceptions import *
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.http import *
from .forms import UserLoginForm
from django.contrib.sessions.models import Session
from django import forms

import requests


def user_login(request):
    logout(request)
    username = password = ''
    if request.method == 'POST':
        context ={}
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
                login(request, user)
                return HttpResponseRedirect('/dashboard')
    else:
        form = UserLoginForm()
        context = {}
        context['form'] = UserLoginForm()
    return render(request, 'users/login.html', context)

def home(request):
    return redirect('dashboard')

def dashboard(request):
    return render(request, 'workhuntr/dashboard.html')


def faq(request):
    return render(request, 'workhuntr/faq.html')
