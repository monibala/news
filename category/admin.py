from django.contrib import admin

from category.models import  category, subcategory

# Register your models here.
admin.site.register(category)
admin.site.register(subcategory)
# admin.site.register(Addsubcategory)