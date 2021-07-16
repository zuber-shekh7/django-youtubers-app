from django.contrib import admin
from django.utils.html import format_html

from .models import Team


class TeamModelAdmin(admin.ModelAdmin):
    def display_picture(self, obj):
        return format_html(f'<img src={obj.photo.url} width=50 />')

    list_display = ('id', 'display_picture',
                    'first_name', 'last_name', 'role',)
    list_display_links = ('display_picture', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'role')
    list_filter = ('role',)


admin.site.register(Team, TeamModelAdmin)
