from django import template

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
