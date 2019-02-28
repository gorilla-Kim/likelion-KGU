from django.contrib import admin
from .models import portfolio

# Register your models here.
class portfolioAdmin(admin.ModelAdmin):
    list_display = ['id', 'likelion']
    list_display_links = ['id', 'likelion']

admin.site.register(portfolio, portfolioAdmin)