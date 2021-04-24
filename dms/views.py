#
# Views for the Dms app
#

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from .models import Message
from .services import MessagingService

#
# View that displays all previous contacts that a user has (previous conversations)
#
@login_required
def contacts(request):
    if request.method == 'POST':
        search_user = request.POST.get('search', None)
        searched = None
        try:
            searched = User.objects.get(username=search_user)
        except:
            messages.error(request, 'You cannot send a message to yourself!')
        if search_user == '' or search_user == request.user.username or searched == None:
            return redirect('contacts')
        return redirect('conversation', search_user)
    all_messages = Message.objects.all().order_by('sent_at')
    contacts_messages = {}
    contact = None
    last_message = None
    for message in all_messages:
        if message.sender == request.user:
            contact = message.recipient
        elif message.recipient == request.user:
            contact = message.sender
        users = [contact, request.user]
        last_message = Message.objects.filter(sender__in=users, recipient__in=users).order_by('sent_at').last()
        contacts_messages[contact] = last_message
    unread_messages = MessagingService.get_unread_messages(request, request.user)
    has_unread_messages = True
    num_of_unread_messages = unread_messages.count()
    if not unread_messages:
        has_unread_messages = False
    return render(request, 'dms/contacts.html', {'contacts_messages': contacts_messages, 'has_unread_messages': has_unread_messages, 'num_of_unread_messages': num_of_unread_messages})

#
# View that displays the messages between two users with most recent first 
#
@login_required
def conversation(request, username):
    contact = User.objects.get(username=username)
    if request.method == 'POST':
        if contact == request.user:
            messages.error(request, 'You cannot send a message to yourself!')
            return redirect('contacts')
        content = request.POST.get('textarea', None)
        MessagingService.send_message(request, sender=request.user, recipient=contact, message=content)
        return redirect('conversation', username)
    users = [request.user, contact]
    all_messages = Message.objects.all().order_by('sent_at')
    conversation = []
    for message in all_messages:
        if message.sender in users and message.recipient in users:
            if message.recipient == request.user:
                MessagingService.mark_as_read(request, message)
            conversation.append(message)
    page = request.GET.get('page', 1)
    conversation = list(reversed(conversation))
    paginator = Paginator(conversation, 4)
    try:
        msgs = paginator.page(page)
    except PageNotAnInteger:
        msgs = paginator.page(1)
    except EmptyPage:
        msgs = paginator.page(paginator.num_pages)
    unread_messages = MessagingService.get_unread_messages(request, request.user)
    has_unread_messages = True
    num_of_unread_messages = unread_messages.count()
    if not unread_messages:
        has_unread_messages = False
    return render(request, 'dms/conversation.html', {'contact': contact, 'msgs': msgs, 'has_unread_messages': has_unread_messages, 'num_of_unread_messages': num_of_unread_messages})

#
# View that displays the info for a conversation and where the user can delete the conversation
#
@login_required
def info(request, username):
    contact = User.objects.get(username=username)
    users = [contact, request.user]
    conversation = Message.objects.filter(sender__in=users, recipient__in=users)
    if not conversation:
        return redirect('contacts')
    if request.method == 'POST':
        for message in conversation:
            message.delete()
        return redirect('contacts')
    unread_messages = MessagingService.get_unread_messages(request, request.user)
    has_unread_messages = True
    num_of_unread_messages = unread_messages.count()
    if not unread_messages:
        has_unread_messages = False
    return render(request, 'dms/info.html', {'has_unread_messages': has_unread_messages, 'num_of_unread_messages': num_of_unread_messages})
