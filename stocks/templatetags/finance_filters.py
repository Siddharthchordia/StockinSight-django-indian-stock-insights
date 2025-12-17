from django import template

register = template.Library()

@register.filter
def to_crore(value):
    try:
        return int(value) / 1e7
    except Exception as e:
        print(e)
        return None