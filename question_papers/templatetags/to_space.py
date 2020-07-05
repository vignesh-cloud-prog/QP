from django import template

register = template.Library()

@register.filter
def to_space(value):
    return value.replace("_" , " ")