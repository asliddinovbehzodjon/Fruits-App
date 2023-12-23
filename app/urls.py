from .views import FruitsViewset
from rest_framework.routers import DefaultRouter
from django.urls import path,include
router = DefaultRouter()
router.register('fruits',FruitsViewset)
urlpatterns = [
    path('',include(router.urls))
]