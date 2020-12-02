from django.shortcuts import render, redirect

from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required
def create_listings(request):
    listings = Listings.objects.all()

    form = ListingsForm(request.POST)
    if request.method == 'POST':
        print('test')
        if form.is_valid():
            listing = form.save()
            listing.refresh_from_db()
            listing.title = form.cleaned_data.get('title')
            listing.description = form.cleaned_data.get('description')
            listing.data = form.cleaned_data.get('date')
            listing.status = form.cleaned_data.get('status')
            listing.save()
            messages.success(request, f'The Listing has been created!')
            return redirect('/current_listings/')
        else:
            messages.error(request, f'Could not create!')

    context = {'listings':listings, 'form':form}
    return render(request, 'listings/create_listings.html', context)

@login_required
def current_listings(request):
    listings = Listings.objects.all()
    context = {'listings': listings}
    return render(request, 'listings/current_listings.html', {'listings': listings})

@login_required
def modify_listings(request, pk):
    listing = Listings.objects.get(id=pk)
    form = ModifyListingForm(instance=listing)

    if request.method == 'POST':
        if form.is_valid():
            listing = form.save()
            listing.refresh_from_db()
            listing.title = form.cleaned_data.get('title')
            listing.status = form.cleaned_data.get('status')
            listing.save()
            messages.success(request, f'Your listing has been updated!')
        return redirect('/current_listings/')

    context = {'form':form}
    return render(request, 'listings/modify_listings.html', context)

@login_required
def delete_listing(request,pk):
    item = Listings.objects.get(id=pk)

    if request.method == 'post':
        item.delete()
        return redirect('/current_listings/')

    context = {'item':item}
    return render(request, 'listings/delete_listing.html', context)