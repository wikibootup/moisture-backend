from django.urls import path, include

from rest_framework import routers

from views import search
from api.views import SearchViewSet

router = routers.DefaultRouter()
router.register('searches', SearchViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('search/<str:text>', search),
]
