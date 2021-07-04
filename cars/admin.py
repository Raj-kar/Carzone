from django.contrib import admin
from .models import Car
from django.utils.html import format_html

# Register your models here.


class CarsAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html(f'<img src="{obj.car_photo.url}" alt="{obj.car_title} img" width="50px" height="45px" style="border-radius: 50%;">')

    image_tag.short_description = 'Image'
    
    list_display = ('id','image_tag', 'car_title', 'city', 'color', 'model',
                    'body_style', 'fuel_type', 'is_featured')
    list_display_links = ('id','image_tag', 'car_title')
    list_editable = ('is_featured',)
    search_fields = ('car_title', 'city', 'model', 'body_style', 'fuel_type')
    list_filter = ('city', 'model', 'body_style', 'fuel_type', 'is_featured')

admin.site.register(Car, CarsAdmin)
