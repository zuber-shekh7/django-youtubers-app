from django.contrib import admin
from django.utils.html import format_html
from .models import Youtuber


class YoutuberModelAdmin(admin.ModelAdmin):
    def display_picture(self, obj):
        return format_html(f'<img src={obj.photo.url} style="border-radius:50%" width=50/>')

    list_display = ('id', 'name', 'display_picture', 'category',
                    'subcribers', 'city', 'is_featured')
    list_display_links = ('id', 'display_picture', 'name')
    list_editable = ('is_featured',)
    list_filter = ('category', 'city', 'camera_type')
    search_fields = ('name', 'category', 'city')


admin.site.register(Youtuber, YoutuberModelAdmin)
