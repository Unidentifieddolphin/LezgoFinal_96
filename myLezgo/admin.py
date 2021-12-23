from django.contrib import admin

from myLezgo.models import Car, Rate, Order

# username: admin, email: zhambyl@gmail.com, password: qwerty

admin.site.register(Car)
admin.site.register(Rate)
admin.site.register(Order)
