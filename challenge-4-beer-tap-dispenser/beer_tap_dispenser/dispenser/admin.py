from django.contrib import admin
from .models import Dispenser, Usage

# Register your models here.

admin.site.register(Dispenser)
admin.site.register(Usage)