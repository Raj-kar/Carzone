from django.contrib import admin
from . import models
from django.utils.html import format_html

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html(f'<img src="{obj.profile.url}" alt="{obj.first_name} img" width="40px" style="border-radius: 50%;">')

    image_tag.short_description = 'Image'

    list_display = ('id', 'image_tag', 'first_name',
                    'last_name', 'designation', 'created_at')
    list_display_links = ('id', 'image_tag', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'designation')
    list_filter = ('designation',)

admin.site.register(models.Team, TeamAdmin)
