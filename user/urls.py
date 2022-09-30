from django.urls import path,include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users',UserViewSet)
router.register('groups',GroupViewSet)
router.register('permission',PermissionViewSet)



urlpatterns = [
    path('', include(router.urls)),
]
