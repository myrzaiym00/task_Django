# from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet

from product.serializers import ProductSerializer
from .models import Product

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer