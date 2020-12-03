from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.response import FileResponse, Http404
from django.shortcuts import render, redirect
from .forms import AddCommentForm, ProfileUpdateForm, UserCreateAccountForm, UserUpdateForm
from .models import Comment, Profile

def create_account(request):
    if request.method == 'POST':
        form = UserCreateAccountForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.email = form.cleaned_data.get('email')
            user.profile.gender = form.cleaned_data.get('gender')
            user.profile.title = form.cleaned_data.get('title')
            user.profile.account_type = form.cleaned_data.get('account_type')
            user.profile.save()
            messages.success(request, f'Your account has been created! You can now login.')
            return redirect('login')
    else:
        form = UserCreateAccountForm()
    return render(request, 'users/create_account.html', {'form': form})

@login_required
def profile(request, username):
    if request.method == 'POST':
        search_user = request.POST.get('search', None)
        if search_user == '':
            return redirect('profile', username)
        return redirect('profile', search_user)
    user = User.objects.get(username=username)
    comments = Comment.objects.filter(profile=user.profile)
    return render(request, 'users/profile.html', {'user':user})

@login_required
def edit_profile(request, username):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
        return redirect('profile', username)
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/edit_profile.html', context)

@login_required
def add_comment(request, username):
    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment = form.cleaned_data.get('comment')
            comment.rating = form.cleaned_data.get('rating')
            comment.company = form.cleaned_data.get('company')
            profile_user = User.objects.get(username=username)
            comment.profile = profile_user.profile
            comment.author = request.user
            comment.save()
            messages.success(request, f'Your comment has been added!')
            return redirect('profile', username)
    else:
        form = AddCommentForm()
    return render(request, 'users/comment.html', {'comment_form': form})
