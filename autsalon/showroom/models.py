from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, blank=True, null=True)
    established_year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, related_name='cars', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    release_year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
