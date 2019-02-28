from django.contrib import admin
from .models import Team

# Register your models here.


class teamAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'discription']
    list_display_links = ['id', 'name']

admin.site.register(Team, teamAdmin)