from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
import logging
# Create your views here.

logger = logging.getLogger(__name__)

@login_required
# @cache_page(60 * 15)
# @vary_on_headers("User-Agent")
def index(request):
    logger.info("Fetching all items from the database")
    item_list = Item.objects.all()
    logger.debug(f"Found {item_list.count()} Items")
    paginator = Paginator(item_list, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'myapp/index.html',context)

# @method_decorator(login_required, name='dispatch')
# class IndexClassView(ListView):
#     model = Item
#     template_name = 'myapp/index.html'
#     context_object_name = 'item_list'

@login_required
def detail(request, id):
    logger.info(f"Fetching details of item with id: {id}")
    try:
        item = get_object_or_404(Item, pk=id)
        logger.debug(f"Fetched details of item with id: {id}")
    except Exception as e:
        logger.error(f"Error fetching the item with id: {id}, {e}")
        raise
    context = {
        'item':item
    }
    return render(request, 'myapp/detail.html', context)

# @method_decorator(login_required, name='dispatch')
# class DetailClassView(DetailView):
#     model = Item
#     template_name = 'myapp/detail.html'
#     context_object_name = 'item'

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

@method_decorator(login_required, name='dispatch')
class ClassCreate_ItemView(CreateView):
    model = Item
    fields = ['item_name', 'item_description', 'item_price', 'item_image']
    template_name = 'myapp/item-form.html'
    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)

# @login_required
# def update_item(request, id):
#     item = Item.objects.get(id = id)
#     form = ItemForm(request.POST or None, instance = item)
#     if form.is_valid():
#             form.save()
#             return redirect('myapp:index')
#     context = {
#         'form': form
#     }
#     return render(request, 'myapp/item-form.html', context)

@method_decorator(login_required, name='dispatch')
class ClassUpdate_ItemView(UpdateView):
    model = Item
    fields = ['item_name', 'item_description', 'item_price', 'item_image']
    template_name = 'myapp/item-form.html'
    
    def get_queryset(self):
        return Item.objects.filter(user_name=self.request.user)

# @login_required
# def delete_item(request, id):
#     item = Item.objects.get(id=id)
#     if request.method == "POST":
#         item.delete()
#         return redirect('myapp:index')
#     return render(request, 'myapp/item-delete.html')

@method_decorator(login_required, name='dispatch')
class ClassDelete_ItemView(DeleteView):
    model = Item
    template_name = 'myapp/item-delete.html'
    success_url = reverse_lazy('myapp:index')

    def get_queryset(self):
        return Item.objects.filter(user_name=self.request.user)