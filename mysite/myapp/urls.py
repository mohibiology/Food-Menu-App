from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>',views.detail, name='detail'),
    path('add/', views.ClassCreate_ItemView.as_view(), name='create_item'),
    path('update/<int:pk>/', views.ClassUpdate_ItemView.as_view(), name='update_item'),
    path('delete/<int:pk>/', views.ClassDelete_ItemView.as_view(), name='delete_item'),
]