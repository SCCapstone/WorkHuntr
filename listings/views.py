from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from dms.services import *

@login_required
def create_listings(request):
    listings = Listings.objects.all()
    form = ListingsForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            listing = form.save(commit=False)
            listing.title = form.cleaned_data.get('title')
            listing.description = form.cleaned_data.get('description')
            if listing.price < 0:
                listing.price = 0
            else:
                listing.price = form.cleaned_data.get('price')
            listing.tag1 = form.cleaned_data.get('tag1')
            listing.tag2 = form.cleaned_data.get('tag2')
            listing.tag3 = form.cleaned_data.get('tag3')
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
    context = {'listings': listings, 'user': request.user}
    return render(request, 'listings/current_listings.html', context)

@login_required
def modify_listings(request, pk):
    listing = Listings.objects.get(id=pk)
    if request.method == 'POST':
        form = ModifyListingForm(request.POST, instance=listing)
        if form.is_valid(): 
            listing = form.save(commit=False)
            listing.refresh_from_db()
            listing.title = form.cleaned_data.get('title')
            if listing.price < 0: 
                listing.price = 0
            else: 
                listing.price = form.cleaned_data.get('price')
            listing.description = form.cleaned_data.get('description')
            listing.tag1 = form.cleaned_data.get('tag1')
            listing.tag2 = form.cleaned_data.get('tag2')
            listing.tag3 = form.cleaned_data.get('tag3')
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
def delete_listing(request, pk):
    item = Listings.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect('/current_listings/')
    return render(request, 'listings/delete_listing.html', {'item':item})

@login_required
def claim_listing(request, pk):
    listing = Listings.objects.get(id=pk)
    listing.status = 'Claimed'
    listing.hunter = request.user
    listing.save()
    return redirect('/current_listings/')

@login_required
def complete_listing(request, pk):
    listing = Listings.objects.get(id=pk)
    listing.status = 'Completed'
    listing.save()
    return redirect('/current_listings/')

@login_required
def issue_payment(request, pk):
    listing = Listings.objects.get(id=pk)
    if request.method == "POST":
        listing.status = 'Payment Issued'
        listing.save()
        # Receipt
        hunter = listing.hunter
        content = 'Receipt for ' + listing.title + ' (' + pk + ').'
        MessagingService.send_message(request, sender=request.user, recipient=hunter, message=content)
        return redirect('/current_listings/')
    else:
        context = {}
        context['form'] = PaymentForm()
        return render(request, "listings/issue_payment.html", context)