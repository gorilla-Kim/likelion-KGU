from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('likelion.urls')),
    path('festival/', include('festival.urls')),
]
