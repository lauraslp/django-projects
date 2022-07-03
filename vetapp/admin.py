from django.contrib import admin
from .models import Client, Pet, Drug, Visit, Card


admin.site.register(Client)
admin.site.register(Pet)
admin.site.register(Drug)
admin.site.register(Visit)
admin.site.register(Card)

