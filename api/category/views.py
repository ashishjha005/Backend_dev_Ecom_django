from rest_framework import viewsets

from .serialize import CategorySerializer 

from .models import Category 

class CategoryViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.all().order_by('name')
    serializer_class=CategorySerializer 