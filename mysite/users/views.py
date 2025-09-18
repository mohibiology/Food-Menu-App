from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def register(request):
    form = UserCreationForm(request.POST)
    if request.method=="POST":
        if form.is_valid():
            form.save()
            return redirect('myapp:index')
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)
