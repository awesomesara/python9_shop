from django.contrib import admin

# Register your models here.

from .models import Category, Product, ProductImage

class ProductImagesInline(admin.TabularInline):
    model = ProductImage
    fields = ['image', ]

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesInline,]
    list_display = ['id', 'title', 'price']
    list_display_links = ['id', 'title']



admin.site.register(Category)
admin.site.register(Product, ProductAdmin)

