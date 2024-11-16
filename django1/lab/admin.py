from django.contrib import admin
from .models import Delivery, Material, Supplier

# Реєструємо моделі для адміністративної панелі
admin.site.register(Delivery)
admin.site.register(Material)
admin.site.register(Supplier)
