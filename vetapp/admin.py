from django.contrib import admin
from .models import Client, Pet, Visit, Card


admin.site.register(Client)
admin.site.register(Pet)
admin.site.register(Visit)
admin.site.register(Card)

