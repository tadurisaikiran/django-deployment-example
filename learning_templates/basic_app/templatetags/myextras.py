from django import templates

register = templates.Library()

@register.filter(name='cut')
def cut(value, arg):
    return value.replace(arg, '')
