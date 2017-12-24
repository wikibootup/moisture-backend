from django.contrib import admin
from django.urls import path, include

from views import search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/search/<str:text>', search),
]
