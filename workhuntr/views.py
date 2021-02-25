from django.contrib.auth.decorators import login_required
from django.core.exceptions import *
from django.shortcuts import render, redirect

def home(request):
    return redirect('dashboard')

def dashboard(request):
    return render(request, 'workhuntr/dashboard.html')

def faq(request):
    return render(request, 'workhuntr/faq.html')
