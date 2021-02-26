from django.contrib import messages
from django.utils import timezone
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
            messages.success(request, f'The listing '+ listing.title +' has been created!')
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
def progress(request, pk):
    listings = Listings.objects.all()
    updates = Update.objects.all()
    ownedListings = MyListingsForm()
    item = Listings.objects.get(id=pk)
    form = UpdateForm(request.POST)
    context = {'listings': listings, 'updates': updates, 'item':item, 'form': form, 'ownedListings': ownedListings}
    if request.method == 'POST':
        if form.is_valid():
                update = form.save(commit=False)
                update.date = timezone.now()
                update.description = form.cleaned_data.get('description')
                update.status = form.cleaned_data.get('status')
                update.listing = item
                update.save()
                item.status = update.status
                item.save()
    return render(request, 'listings/progress.html', context)

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
            messages.success(request, f'Your listing '+ listing.title + ' has been modified!')
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

def return_listing(request, pk):
    listing = Listings.objects.get(id=pk)
    listing.status = 'Strutting'
    listing.hunter = request.user
    listing.save()
    messages.success(request, f'Listing  ' + str(listing.title) + ' has been returned to current listings. ' + str(listing.huntee) + ' has been notified!')
    huntee = listing.huntee
    content = 'Your listing ' + listing.title + ' has been returned to current listings by ' + str(listing.hunter) + '.'
    MessagingService.send_message(request, sender=request.user, recipient=huntee, message=content)
    return redirect('/current_listings/')


@login_required
def claim_listing(request, pk):
    listing = Listings.objects.get(id=pk)
    listing.status = 'Claimed'
    listing.hunter = request.user
    listing.save()
    messages.success(request, f'Listing  ' + str(listing.title) + ' has been marked claimed! ' + str(listing.huntee) + ' has been notified!')
    huntee = listing.huntee
    content = 'Your listing ' + listing.title + ' has been marked claimed by '\
              + str(listing.hunter) + '! Please contact this user if more instructions are needed.'
    MessagingService.send_message(request, sender=request.user, recipient=huntee, message=content)
    return redirect('/current_listings/')

@login_required
def complete_listing(request, pk):
    listing = Listings.objects.get(id=pk)
    listing.status = 'Completed'
    listing.save()
    messages.success(request, f'Listing  ' + str(listing.title) + ' has been marked completed! ' + str(listing.huntee) + ' has been notified!')
    huntee = listing.huntee
    content = 'Your listing ' + listing.title + ' has been marked completed by ' + str(listing.hunter) + '! Please issue payment for completed listing.'
    MessagingService.send_message(request, sender=request.user, recipient=huntee, message=content)
    return redirect('/current_listings/')

@login_required
def issue_payment(request, pk):
    listing = Listings.objects.get(id=pk)
    if request.method == "POST":
        listing.status = 'Payment Issued'
        listing.save()
        messages.success(request, f'Payment has been issued to ' + str(listing.hunter) + ' in the amount of $' + str(listing.price) + '!')
        # Receipt
        hunter = listing.hunter
        content = 'Receipt for ' + listing.title +  ' { Listing number:' +' (' + pk + ') ' + ', Listing Price: $' + str(listing.price) + \
                  ', Completed by: ' + str(listing.hunter) + ', Listed by: ' + str(listing.huntee) + ' }'
        MessagingService.send_message(request, sender=request.user, recipient=hunter, message=content)
        return redirect('/current_listings/')
    else:
        context = {'form': PaymentForm(), 'listing':listing}
        return render(request, "listings/issue_payment.html", context)

@login_required
def receipt(request, pk):
    listing = Listings.objects.get(id=pk)
    if request.method == "POST":
        return redirect('/current_listings/')
    else:
        context = {'listing': listing}
        return render(request, 'listings/receipt.html', context)