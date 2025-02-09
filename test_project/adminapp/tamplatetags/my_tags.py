from django import template
from django.conf import settings

register = template.Library()

def media_folder_products(string):
    if not string:
        string = '/media/media/default.jpg'

    return '{}{}'.format(settings.MEDIA_URL, string)

@register.filter(name='media_folder_users')
def media_folder_users(string):
    if not string:
        string = '/media/media/default.jpg'

    return '{}{}'.format(settings.MEDIA_URL, string)

register.filter('media_folder_products', media_folder_products)