from django.contrib import admin
from .models import Portfolio

# Register your models here.
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['id', 'likelion']
    list_display_links = ['id', 'likelion']

admin.site.register(Portfolio, PortfolioAdmin)