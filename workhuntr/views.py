from django.core.exceptions import *
from django.shortcuts import render, redirect, HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
import requests  # Requests will need to be installed

def home(request):
  return redirect('login')

@login_required
def dashboard(request):
  return render(request, 'workhuntr/dashboard.html')

