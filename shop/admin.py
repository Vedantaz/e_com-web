from django.contrib import admin
from django.contrib.admin.decorators import register

# Register your models here.
from . models import Contact, OrderUpdate, Product , Order , OrderUpdate

admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(OrderUpdate)








