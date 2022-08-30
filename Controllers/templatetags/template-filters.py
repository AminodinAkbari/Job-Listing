from django import template

register = template.Library()

@register.filter()
def find_state(value , state):
    return value.filter(state = state)

@register.filter()
def find_value(arg , key):
    return arg.get(key)

@register.filter()
def last_item_in_list(list):
    pass

# @register.filter()
# def JSON_BTN(url , pk):
#     return reverse('url', kwargs ={'pk' : pk})
