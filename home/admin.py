from django.contrib import admin

from .models import *

@admin.register(slider)
class AdminSlider(admin.ModelAdmin):
    list_display = ['image','date','title','desc']

@admin.register(news_trend)
class AdminSlider(admin.ModelAdmin):
    list_display = ['head1','head2','head3','image','date','writer_name','writer_image','title',]    

admin.site.register(gallery)   
admin.site.register(popular)
admin.site.register(features)