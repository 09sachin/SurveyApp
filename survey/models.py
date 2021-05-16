from django.db import models


class Survey(models.Model):
    name = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    phone = models.CharField(max_length=1000)
    rating = models.CharField(max_length=1000)

