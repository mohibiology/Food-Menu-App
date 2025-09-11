from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
# Create your views here.
def index(request):
    item_list = Item.objects.all()
    context = {
        "item_list": item_list
    }
    return render(request, 'myapp/index.html',context)

def item(request):
    return HttpResponse("Item")

def detail(request, id):
    item = Item.objects.get(id=id)
    context = {
        "item":item
    }
    return render(request, 'myapp/detail.html', context)