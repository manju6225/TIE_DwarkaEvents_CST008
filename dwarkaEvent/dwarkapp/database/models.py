from django.db import models


class connect(models.Model):
    name = models.CharField(max_length=25)

    city = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    pincode = models.BigIntegerField(max_length=10)
    event = models.CharField(max_length=50)
    cc = models.BigIntegerField(max_length=20)
    exp = models.DateField()
    cvv = models.IntegerField(max_length=5)
