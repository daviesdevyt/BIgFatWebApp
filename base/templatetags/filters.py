from django import template
from django.http import QueryDict

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter(name='range')
def num_range(end, start=1):
    return range(start, end+1)

@register.filter
def rewrite_base(text):
    return text.replace("__", " ")

@register.filter(name='truncate')
def truncate_and_remove_dots(value, arg):
    return value[:int(arg)]

@register.filter(name='fullz_name')
def fullz_name(full_name):
    fname, *lname = full_name.split()
    return fname +" "+ lname[0][0].upper() + "."

@register.filter(name='paginator')
def urlencode(url_dict: QueryDict):
    url_dict = url_dict.copy()
    try:
        popped = url_dict.pop("page")
        if popped:
            return ""
    except KeyError:
        pass
    return url_dict.urlencode()