from django import template

register = template.Library()

@register.filter(name='is_manager_tag')
def is_manager_tag(user):
    return user.groups.filter(name='manager').exists()