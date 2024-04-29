from django.db import models


class CarSpecs(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    body = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.brand + ' ' + self.model + ' '
