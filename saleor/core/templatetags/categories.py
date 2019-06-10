from django import template

register = template.Library()


@register.filter
def categorify(text):
    return ", ".join([i.title() for i in text.split(',')])


@register.filter
def titleify(text):
    return text.title()
