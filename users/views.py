from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import UserCreateAccountForm, UserUpdateForm, ProfileUpdateForm

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
def profile(request):
  return render(request, 'users/profile.html')

@login_required
def edit_profile(request):
  if request.method == 'POST':
    u_form = UserUpdateForm(request.POST, instance=request.user)
    p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
    if u_form.is_valid() and p_form.is_valid():
      u_form.save()
      p_form.save()
      messages.success(request, f'Your account has been updated!')
      return redirect('profile')
  else:
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)
  context = {
    'u_form': u_form,
    'p_form': p_form
  }
  return render(request, 'users/edit_profile.html', context)
