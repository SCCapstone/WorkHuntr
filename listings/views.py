from django.shortcuts import render
from django.http import Http404

from .models import Listings

# Create your views here.

def current_listings(request):
    listings = Listings.objects.order_by('-date')[:5]
    context = {'listings': listings}
    return render(request, 'listings/current_listings.html', context)

