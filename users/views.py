from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import AddCommentForm, ProfileUpdateForm, UserCreateAccountForm, UserUpdateForm, AddSkillForm, AddHistoryForm
from .models import Comment, Skill, History

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
            user.profile.birthday = form.cleaned_data.get('birthday')
            user.profile.current_employment = form.cleaned_data.get('current_employment')
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
        searched = None
        try:
            searched = User.objects.get(username=search_user)
        except:
            print('User Not Found')
        if search_user == '' or searched == None:
            return redirect('profile', username)
        return redirect('profile', search_user)
    user = User.objects.get(username=username)
    comments = Comment.objects.filter(profile=user.profile)
    skills = Skill.objects.filter(profile=user.profile)
    histories = History.objects.filter(profile=user.profile)
    return render(request, 'users/profile.html', {'user':user, 'comments':comments, 'skills':skills, 'histories':histories})

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

@login_required
def add_skill(request, username):
    if request.method == 'POST':
        s_form = AddSkillForm(request.POST)
        if s_form.is_valid():
            skill = s_form.save(commit=False)
            skill.skill = s_form.cleaned_data.get('skill')
            profile_user = User.objects.get(username=username)
            skill.profile = profile_user.profile
            skill.author = request.user
            skill.save()
            messages.success(request, f'Your skill has been added!')
            return redirect('profile', username)
    else:
        s_form = AddSkillForm()
    return render(request, 'users/skill.html', {'skill_form': s_form})

@login_required
def add_history(request, username):
    if request.method == 'POST':
        h_form = AddHistoryForm(request.POST)
        if h_form.is_valid():
            history = h_form.save(commit=False)
            history.description = h_form.cleaned_data.get('description')
            history.company = h_form.cleaned_data.get('company')
            history.start_date = h_form.cleaned_data.get('start_date')
            history.end_date = h_form.cleaned_data.get('start_date')
            profile_user = User.objects.get(username=username)
            history.profile = profile_user.profile
            history.author = request.user
            history.save()
            messages.success(request, f'Your work history has been added!')
            return redirect('profile', username)
    else:
        h_form = AddHistoryForm()
    return render(request, 'users/history.html', {'h_form': h_form})