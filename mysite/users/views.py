from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    form = RegisterForm(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Pakhair raghle {username}, sta account jor sho')
            return redirect('users:login')
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)

def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')

@login_required
def profile(request):
    return render(request, 'users/profile.html')