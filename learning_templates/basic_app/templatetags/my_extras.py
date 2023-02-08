from django import template

register = template.Library()

@register.filter(name='new_cut')
def new_cut(value, arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg,'')

# register.filter('new_cut', new_cut)
