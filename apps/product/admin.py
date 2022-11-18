from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Brands)

class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'description', 'status']
    list_filter = ['status',]
    search_fields = ['title', 'description', 'id']
    # date_hierarchy = 'createdAt'

admin.site.register(Departments, DepartmentsAdmin)

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'description', 'department', 'status']
    list_filter = ['department', 'status']
    search_fields = ['title', 'description', 'id']
    # date_hierarchy = 'createdAt'

admin.site.register(Categories, CategoriesAdmin)

admin.site.register(SubCategories)
admin.site.register(Products)
