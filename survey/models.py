from django.db import models


class Survey(models.Model):
    name = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    phone = models.CharField(max_length=1000)
    rating = models.CharField(max_length=1000)


class Product1(models.Model):
    p1q1 = models.CharField(max_length=1000)
    p1q2 = models.CharField(max_length=1000)
    p1q3 = models.CharField(max_length=1000)
    p1q4 = models.CharField(max_length=1000)
    name = models.ForeignKey('Name', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name.name


class Product2(models.Model):
    p2q1 = models.CharField(max_length=1000)
    p2q2 = models.CharField(max_length=1000)
    p2q3 = models.CharField(max_length=1000)
    p2q4 = models.CharField(max_length=1000)
    name = models.ForeignKey('Name', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name.name


class Name(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
