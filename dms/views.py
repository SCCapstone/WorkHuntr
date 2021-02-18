from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Message
from .services import MessagingService

@login_required
def contacts(request):
    if request.method == 'POST':
        search_user = request.POST.get('search', None)
        searched = None
        try:
            searched = User.objects.get(username=search_user)
        except:
            print('User Not Found')
        if search_user == '' or searched == None:
            return redirect('contacts')
        return redirect('conversation', search_user)
    all_messages = Message.objects.all().order_by('sent_at')
    contacts = []
    contact = None
    last_message = None
    for message in all_messages:
        if message.sender == request.user:
            contact = message.recipient
        elif message.recipient == request.user:
            contact = message.sender
        users = [contact, request.user]
        contacts.append(contact)
        last_message = Message.objects.filter(sender__in=users, recipient__in=users).order_by('sent_at').last()
    contacts = set(contacts)
    return render(request, 'dms/contacts.html', {'contacts': contacts, 'last_message': last_message})

@login_required
def conversation(request, username):
    contact = User.objects.get(username=username)
    if request.method == 'POST':
        content = request.POST.get('textarea', None)
        MessagingService.send_message(request, sender=request.user, recipient=contact, message=content)
        return redirect('conversation', username)
    users = [request.user, contact]
    all_messages = Message.objects.all().order_by('sent_at')
    conversation = []
    for message in all_messages:
        if message.sender in users and message.recipient in users:
            conversation.append(message)
    return render(request, 'dms/conversation.html', {'contact': contact, 'conversation': conversation})

@login_required
def info(request, username):
    if request.method == 'POST':
        contact = User.objects.get(username=username)
        users = [contact, request.user]
        conversation = Message.objects.filter(sender__in=users, recipient__in=users)
        for message in conversation:
            message.delete()
        return redirect('contacts')
    return render(request, 'dms/info.html')
