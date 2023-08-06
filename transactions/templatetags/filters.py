from django import template

register = template.Library()

@register.filter
def get_track_id(value):
    return value.split("/")[-1]
