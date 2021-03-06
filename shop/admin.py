from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
    )
    prepopulated_fields = {
        'slug': ('name', ),
    }


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'stock',
        'available',
        'createdAt',
        'updatedAt',
    )
    list_editable = (
        'price',
        'stock',
        'available',
    )
    prepopulated_fields = {
        'slug': ('name', ),
    }
    list_per_page = 20


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)