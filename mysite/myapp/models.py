from django.db import models

# Create your models here.
class Item(models.Model):

    def __str__(self):
        return self.item_name
    
    item_name = models.CharField(max_length=100)
    item_description = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default='https://thumbs.dreamstime.com/b/laughing-cooking-couple-kitchen-silly-meal-prep-morning-joke-smile-apartment-relationship-man-affection-339924493.jpg')