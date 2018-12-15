from django import template
from ..models import ProductReview

register = template.Library()


@register.simple_tag()
def calculate_rating(product):
    reviews = ProductReview.objects.filter(product=product)
    if reviews.count() == 0:
        return 0
    ratings = 0
    for review in reviews:
        ratings += review.stars
    ratings /= reviews.count()
    return round(ratings)


@register.filter
def subtract(value, arg):
    return value - arg

@register.simple_tag()
def create_stars(value):
    return "x" * value + "o" * (5 - value)
