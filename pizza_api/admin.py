from django.contrib import admin
from .models import Pizza, Topping, Order, Price, User

# Register your models here.
admin.site.register(Pizza)
admin.site.register(Price)
admin.site.register(Topping)
admin.site.register(Order)
admin.site.register(User)