from django import template
register = template.Library() 

@register.filter(name='set')
def to_set(value): 
    return set(value)