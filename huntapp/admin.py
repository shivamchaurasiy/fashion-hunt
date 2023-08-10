from django.contrib import admin
from huntapp.models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['cid', 'cname']
