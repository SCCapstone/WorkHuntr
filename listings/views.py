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
            listing.price = form.cleaned_data.get('price')
            listing.tag1 = form.cleaned_data.get('tag1')
            listing.tag2 = form.cleaned_data.get('tag2')
            listing.tag3 = form.cleaned_data.get('tag3')
            listing.status = form.cleaned_data.get('status')
            listing.huntee = request.user
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

    if request.method == 'POST':
        form = ModifyListingForm(request.POST, instance=listing)
        if form.is_valid(): 
            listing = form.save(commit=False)
            listing.refresh_from_db()
            listing.title = form.cleaned_data.get('title')
            listing.price = form.cleaned_data.get('price')
            listing.description = form.cleaned_data.get('description')
            listing.tag1 = form.cleaned_data.get('tag1')
            listing.tag2 = form.cleaned_data.get('tag2')
            listing.tag3 = form.cleaned_data.get('tag3')
            listing.status = form.cleaned_data.get('status')
            listing.save()
            messages.success(request, f'Your listing has been updated!')
        return redirect('/current_listings/')
    else:
        form = ModifyListingForm(instance=listing)
    modifiable = False
    if request.user == listing.huntee:
        modifiable = True
    context = {'listing':listing, 'form':form, 'modifiable': modifiable}
    return render(request, 'listings/modify_listings.html', context)

@login_required
def delete_listing(request,pk):
    item = Listings.objects.get(id=pk)

    if request.method == "POST":
        item.delete()
        return redirect('/current_listings/')

    context = {'item':item}
    return render(request, 'listings/delete_listing.html', {'item':item})

@login_required
def claim_listing(request, pk):
    listing = Listings.objects.get(id=pk)
    print(pk)
    listing.status = 'Claimed'
    listing.hunter = request.user
    listing.save()
    return redirect('/current_listings/')