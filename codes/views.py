from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .forms import CodeForm
from .models import Code

def verify_view(request):
    form = CodeForm(request.POST or None)
    user = User.objects.get(username=request.user)
    code = user.code
    code_user = f"{user.username} : {user.code}"
    if not request.POST:
        pass
    if form.is_valid():
        num = form.cleaned_data.get('number')
        if str(code) == num:
            code.save()
            login(request, user)
            return redirect('dashboard')
        else:
            return redirect('login')
    return render(request, 'codes/verify.html', {'form' : form})