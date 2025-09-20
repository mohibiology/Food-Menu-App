from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list': item_list
    }
    return render(request, 'myapp/index.html',context)

@login_required
def detail(request, id):
    item = Item.objects.get(id=id)
    context = {
        'item':item
    }
    return render(request, 'myapp/detail.html', context)

@login_required
def create_item(request):
    form = ItemForm(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            form.save()
            return redirect('myapp:index')
    context ={
        'form': form
    }
    return render(request, 'myapp/item-form.html', context)

@login_required
def update_item(request, id):
    item = Item.objects.get(id = id)
    form = ItemForm(request.POST or None, instance = item)
    if form.is_valid():
            form.save()
            return redirect('myapp:index')
    context = {
        'form': form
    }
    return render(request, 'myapp/item-form.html', context)

@login_required
def delete_item(request, id):
    item = Item.objects.get(id=id)
    if request.method == "POST":
        item.delete()
        return redirect('myapp:index')
    return render(request, 'myapp/item-delete.html')