from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Account)
admin.site.register(models.Classification)
admin.site.register(models.Product)
admin.site.register(models.ShoppingCart)
admin.site.register(models.Type)



