from django.contrib import admin

# Register your models here.

from . models import Catergory, Product

@admin.register(Catergory)
class CategoryAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('title',)}

