from django.db import models
from django.utils.text import slugify


class Review(models.Model):
    user_name = models.CharField(max_length=100)
    review_text = models.TextField()
    rating = models.IntegerField()
    owner_comment = models.TextField(default='')