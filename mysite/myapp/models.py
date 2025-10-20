from django.utils import timezone
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from .managers import ItemManager
from django import forms
# Create your models here.
class Item(models.Model):
    class Meta:
        indexes = [
            models.Index(fields=['user_name', 'item_price']),
        ]

    def __str__(self):
        return self.item_name
    
    def get_absolute_url(self):
        return reverse('myapp:index')
    
    def success_url(self):
        return reverse('myapp:index')
    
    def delete(self, using = None, keep_parents = False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
    
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=100, db_index=True)
    item_description = models.CharField(max_length=200)
    item_price = models.DecimalField(max_digits=6,decimal_places=2, db_index=True)
    item_image = models.URLField(max_length=500, default='https://thumbs.dreamstime.com/b/laughing-cooking-couple-kitchen-silly-meal-prep-morning-joke-smile-apartment-relationship-man-affection-339924493.jpg')
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True,blank=True)

    objects = ItemManager()

class Category(models.Model):

    def __str__(self):
        return self.name


    name = models.CharField(max_length=100)
    added_on = models.DateField(auto_now=True)