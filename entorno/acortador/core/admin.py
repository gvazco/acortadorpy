from django.contrib import admin
from .models import Enlace

# Register your models here.
@admin.register(Enlace)
class Administrador(admin.ModelAdmin):
    pass 
