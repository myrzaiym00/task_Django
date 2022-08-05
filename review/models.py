from django.db import models
from django.contrib.auth import get_user_model

from product.models import Product

User = get_user_model()

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    rating = models.IntegerField(choices=[(1,1), (2,2), (3,3), (4,4), (5,5)])