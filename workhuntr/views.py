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

#@login_required
#def create_listing(request):
#  return render(request, 'workhuntr/create_listing.html')

#@login_required
#def current_listings(request):
#  return render(request, 'listings/current_listings.html')

#@login_required
#def modify_listings(request):
#  return render(request, 'workhuntr/modify_listings.html')
