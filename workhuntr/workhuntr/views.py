from django.core.exceptions import *
from django.shortcuts import render, redirect, HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import requests  # Requests will need to be imported

@csrf_exempt
def login(request):
  return render(request, 'login.html')

@csrf_exempt
def create_account(request):
  return render(request, 'create_account.html')

@csrf_exempt
def dashboard(request):
  return render(request, 'dashboard.html')

@csrf_exempt
def current_listings(request):
  return render(request, 'current_listings.html')

@csrf_exempt
def modify_listings(request):
  return render(request, 'modify_listings.html')

@csrf_exempt
def profile(request):
  return render(request, 'profile.html')

def home(request):
  return render(request, 'home.html')