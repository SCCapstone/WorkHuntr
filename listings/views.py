from django.shortcuts import render, redirect

from .forms import *
from .models import *

# Create your views here.


def create_listings(request):
    listings = Listings.objects.all()

    form = ListingsForm()

    if request.method == 'post':
        form = ListingsForm(request.post)
        if form.is_valid():
            form.save()
        return redirect('/current_listings')

    context = {'listings':listings, 'form':form}
    return render(request, 'listings/create_listings.html', context)

def current_listings(request):
    listings = Listings.objects.all()
    context = {'listings': listings}
    return render(request, 'listings/current_listings.html', context)

def modify_listings(request, pk):
    listing = Listings.objects.get(id=pk)

    form = ListingsForm(instance=listing)

    if request.method == 'post':
        form = ListingsForm(request.post, instance=listing)
        if form.is_valid():
            form.save()
        return redirect('/current_listings')

    context = {'form':form}
    return render(request, 'listings/modify_listings.html')

def delete_listing(request,pk):
    item = Listings.objects.get(id=pk)

    if request.method == 'post':
        item.delete()
        return redirect('/current_listings')

    context = {'item':item}
    return render(request, 'listings/delete_listing.html')