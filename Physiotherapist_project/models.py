from django.db import models
from django.contrib.auth.models import User


class Physiotherapist(models.Model):
    name_of_physiotherapist = models.CharField(max_length=64)

    def __str__(self):
        return self.name_of_physiotherapist


class Product(models.Model):
    name_of_product = models.CharField(max_length=64)
    physiotherapist = models.ForeignKey(Physiotherapist, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_of_product


class Session(models.Model):
    name_of_session = models.CharField(max_length=64)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_of_session


class Price(models.Model):
    value = models.DecimalField(max_digits=10, decimal_places=3)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.value)


class Booking(models.Model):
    physiotherapist = models.ForeignKey(Physiotherapist, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    price = models.ForeignKey(Price, on_delete=models.CASCADE)
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.physiotherapist)

    class Meta:
        unique_together = ('physiotherapist', 'date',)
