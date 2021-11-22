from django.contrib import admin

# Register your models here.
from .models import Proj

@admin.register(Proj)
class ProjAdmin(admin.ModelAdmin):
    list_display = ("Nome", "Tel","email")