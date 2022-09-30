from .serializers import *
from .models import *
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import Group, Permission

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=(AllowAny,)
    pagination_class = None
    
class GroupViewSet(viewsets.ModelViewSet):
    queryset=Group.objects.all()
    serializer_class=GroupSerializer
    pagination_class = None
    
class PermissionViewSet(viewsets.ModelViewSet):
    queryset=Permission.objects.all()
    serializer_class=PermissionSerializer
    pagination_class = None