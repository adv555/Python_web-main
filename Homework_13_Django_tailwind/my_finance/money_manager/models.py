from django.db import models
from django.utils.timezone import now
from django.conf import settings


# Create your models here.

class Income(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.TextField()
    created = models.DateTimeField(default=now)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.id}, {self.amount}, {self.description}, {self.created}'  # NOQA


class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created = models.DateTimeField(default=now)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.id}, {self.amount}, {self.description}, {self.created}'  # NOQA


class Category(models.Model):
    name = models.CharField(max_length=200)
    # income = models.ManyToManyField(Income)
    # expense = models.ManyToManyField(Expense)


    def __str__(self):
        return f'{self.id}, {self.name}'  # NOQA
