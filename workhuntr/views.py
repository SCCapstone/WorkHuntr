from django.contrib.auth.decorators import login_required
from django.core.exceptions import *
from django.shortcuts import render, redirect, HttpResponse
from django.template import loader
import requests

def home(request):
    return redirect('login')

@login_required
def dashboard(request):
    return render(request, 'workhuntr/dashboard.html')

