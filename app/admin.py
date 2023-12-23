from django.contrib import admin
# Register your models here.
from .models import FruitsModel
@admin.register(FruitsModel)
class FruitsAdmin(admin.ModelAdmin):
    list_display = ['id','name','cost']
    list_editable = ['name']
    list_display_links = ['id']
    list_per_page = 10
    search_fields = ['name','description','cost']