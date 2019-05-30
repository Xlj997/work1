from django import template
from .. import models
from django.core import serializers
register = template.Library()


@register.simple_tag
def All():
    products = models.Product.objects.all()

    # result = serializers.serialize("json", products)
    # print(result)

    return products