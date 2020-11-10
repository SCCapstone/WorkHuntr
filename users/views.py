from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserCreateAccountForm

def create_account(request):
  if request.method == 'POST':
    form = UserCreateAccountForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      messages.success(request, f'Your account has been created! You can now login.')
      return redirect('login')
  else:
    form = UserCreateAccountForm()
  return render(request, 'users/create_account.html', {'form': form})

@login_required
def profile(request):
  return render(request, 'users/profile.html')
