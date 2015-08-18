#!/usr/bin/env python
from django import template

register = template.Library()

# multiply filter
@register.filter(name = 'mul')
def mul(value, arg):
    return value * arg