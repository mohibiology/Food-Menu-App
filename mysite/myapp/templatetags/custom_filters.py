from django import template

register = template.Library()

@register.filter
def discount(price, discount_percentage):
    return int(price) * (1 - discount_percentage / 100)