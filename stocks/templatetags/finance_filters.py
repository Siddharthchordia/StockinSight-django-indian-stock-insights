from django import template

register = template.Library()

@register.filter
def to_crore(value):
    try:
        return value / 1e7
    except:
        return None