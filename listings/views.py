from django.contrib import messages
from django.db.models import Q
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from dms.services import *

@login_required
def create_listings(request):
    if request.user.profile.account_type != 'Huntee':
        return redirect('current_listings')
    listings = Listings.objects.all()
    form = ListingsForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            listing = form.save(commit=False)
            listing.title = form.cleaned_data.get('title')
            listing.description = form.cleaned_data.get('description')
            listing.price = form.cleaned_data.get('price')
            listing.tag_one = form.cleaned_data.get('tag_one')
            listing.tag_two = form.cleaned_data.get('tag_two')
            listing.tag_three = form.cleaned_data.get('tag_three')
            listing.huntee = request.user
            listing.save()
            messages.success(request, f'Your listing "'+ listing.title +'" has been created!')
            return redirect('current_listings')
        else:
            messages.error(request, f'Error: The listing could not be created!')
    unread_messages = MessagingService.get_unread_messages(request, request.user)
    has_unread_messages = True
    num_of_unread_messages = unread_messages.count()
    if not unread_messages:
        has_unread_messages = False
    context = {'listings':listings, 'form':form, 'has_unread_messages':has_unread_messages, 'num_of_unread_messages':num_of_unread_messages}
    return render(request, 'listings/create_listings.html', context)

@login_required
def current_listings(request):
    search_query = request.GET.get('search', '')
    if search_query:
        listings = Listings.objects.filter(Q(title__icontains=search_query) | Q(tag_one__icontains=search_query) | Q(tag_two__icontains=search_query) | Q(tag_three__icontains=search_query))
    else:
        listings = Listings.objects.all()
    unread_messages = MessagingService.get_unread_messages(request, request.user)
    has_unread_messages = True
    num_of_unread_messages = unread_messages.count()
    if not unread_messages:
        has_unread_messages = False
    context = {'listings': listings, 'user': request.user, 'has_unread_messages': has_unread_messages, 'num_of_unread_messages': num_of_unread_messages}
    return render(request, 'listings/current_listings.html', context)

@login_required
def progress(request, pk):
    listings = Listings.objects.all()
    updates = Update.objects.all()
    select_page = request.GET.get('selected', '')
    if select_page:
        item = Listings.objects.get(title=select_page)
    else: 
        item = Listings.objects.get(id=pk)
    if request.user != item.hunter or request.user != item.huntee:
        return redirect('current_listings')
    form = UpdateForm(request.POST)
    unread_messages = MessagingService.get_unread_messages(request, request.user)
    has_unread_messages = True
    num_of_unread_messages = unread_messages.count()
    if not unread_messages:
        has_unread_messages = False
    context = {'listings': listings, 'updates': updates, 'item':item, 'form': form, 'has_unread_messages': has_unread_messages, 'num_of_unread_messages': num_of_unread_messages}
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
    if request.user == listing.huntee and listing.status == 'Strutting':
        if request.method == 'POST':
            form = ModifyListingForm(request.POST, instance=listing)
            if form.is_valid():
                listing = form.save(commit=False)
                listing.refresh_from_db()
                listing.title = form.cleaned_data.get('title')
                listing.price = form.cleaned_data.get('price')
                listing.description = form.cleaned_data.get('description')
                listing.tag_one = form.cleaned_data.get('tag_one')
                listing.tag_two = form.cleaned_data.get('tag_two')
                listing.tag_three = form.cleaned_data.get('tag_three')
                listing.save()
                messages.success(request, f'Your listing "'+ listing.title + '" has been modified!')
            return redirect('current_listings')
        else:
            form = ModifyListingForm(instance=listing)
        modifiable = False
        if request.user == listing.huntee:
            modifiable = True
        unread_messages = MessagingService.get_unread_messages(request, request.user)
        has_unread_messages = True
        num_of_unread_messages = unread_messages.count()
        if not unread_messages:
            has_unread_messages = False
        context = {'listing':listing, 'form':form, 'modifiable': modifiable, 'has_unread_messages': has_unread_messages, 'num_of_unread_messages': num_of_unread_messages}
        return render(request, 'listings/modify_listings.html', context)
    else:
        return redirect('current_listings')

@login_required
def delete_listing(request, pk):
    item = Listings.objects.get(id=pk)
    if request.user == item.huntee:
        if request.method == "POST":
            item.delete()
            return redirect('current_listings')
    else:
        return redirect('current_listings')
    unread_messages = MessagingService.get_unread_messages(request, request.user)
    has_unread_messages = True
    num_of_unread_messages = unread_messages.count()
    if not unread_messages:
        has_unread_messages = False
    return render(request, 'listings/delete_listing.html', {'item':item, 'has_unread_messages':has_unread_messages, 'num_of_unread_messages':num_of_unread_messages})

@login_required
def return_listing(request, pk):
    listing = Listings.objects.get(id=pk)
    if request.user != listing.hunter:
        return redirect('current_listings')
    listing.status = 'Strutting'
    listing.hunter = request.user
    listing.save()
    messages.success(request, f'Listing ' + str(listing.title) + ' has been returned to current listings. ' + str(listing.huntee) + ' has been notified!')
    huntee = listing.huntee
    content = 'Your listing ' + listing.title + ' has been returned to current listings by ' + str(listing.hunter) + '.'
    MessagingService.send_message(request, sender=request.user, recipient=huntee, message=content)
    return redirect('current_listings')

@login_required
def claim_listing(request, pk):
    listing = Listings.objects.get(id=pk)
    if listing.status == 'Claimed':
        return redirect('current_listings')
    listing.status = 'Claimed'
    listing.hunter = request.user
    listing.save()
    messages.success(request, f'Listing  ' + str(listing.title) + ' has been marked claimed! ' + str(listing.huntee) + ' has been notified!')
    huntee = listing.huntee
    content = 'Your listing ' + listing.title + ' has been marked claimed by ' + str(listing.hunter) + '! Please contact this user if more instructions are needed.'
    MessagingService.send_message(request, sender=request.user, recipient=huntee, message=content)
    return redirect('current_listings')

@login_required
def complete_listing(request, pk):
    listing = Listings.objects.get(id=pk)
    if request.user != listing.huntee:
        return redirect('current_listings')
    listing.status = 'Completed'
    listing.save()
    messages.success(request, f'Listing  ' + str(listing.title) + ' has been marked completed! ' + str(listing.huntee) + ' has been notified!')
    huntee = listing.huntee
    content = 'Your listing ' + listing.title + ' has been marked completed by ' + str(listing.hunter) + '! Please issue payment for completed listing.'
    MessagingService.send_message(request, sender=request.user, recipient=huntee, message=content)
    return redirect('current_listings')

@login_required
def issue_payment(request, pk):
    listing = Listings.objects.get(id=pk)
    if request.user != listing.huntee:
        return redirect('current_listings')
    if request.method == "POST":
        listing.status = 'Payment Issued'
        listing.save()
        messages.success(request, f'Payment has been issued to ' + str(listing.hunter) + ' in the amount of $' + str(listing.price) + '!')
        hunter = listing.hunter
        content = 'Receipt for ' + listing.title +  ' { Listing number:' +' (' + pk + ') ' + ', Listing Price: $' + str(listing.price) + ', Completed by: ' + str(listing.hunter) + ', Listed by: ' + str(listing.huntee) + ' }'
        MessagingService.send_message(request, sender=request.user, recipient=hunter, message=content)
        return redirect('current_listings')
    else:
        unread_messages = MessagingService.get_unread_messages(request, request.user)
        has_unread_messages = True
        num_of_unread_messages = unread_messages.count()
        if not unread_messages:
            has_unread_messages = False
        context = {'form': PaymentForm(), 'listing':listing, 'has_unread_messages':has_unread_messages, 'num_of_unread_messages':num_of_unread_messages}
        return render(request, "listings/issue_payment.html", context)

@login_required
def receipt(request, pk):
    listing = Listings.objects.get(id=pk)
    if request.user != listing.huntee or request.user != listing.hunter:
        return redirect('current_listings')
    if request.method == "POST":
        return redirect('current_listings')
    else:
        unread_messages = MessagingService.get_unread_messages(request, request.user)
        has_unread_messages = True
        num_of_unread_messages = unread_messages.count()
        if not unread_messages:
            has_unread_messages = False
        context = {'listing': listing, 'has_unread_messages': has_unread_messages, 'num_of_unread_messages':num_of_unread_messages,}
        return render(request, 'listings/receipt.html', context)
