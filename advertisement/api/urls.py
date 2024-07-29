from django.urls import path, include
from .views import AdvertisementViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', AdvertisementViewSet, basename='advertisement')

urlpatterns = [
    path('', include(router.urls), name='advertisement')
]
