from typing import List
from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
import datetime

# Create your models here.


class Customer(models.Model):
    """ Model for customer table """
    name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=12)

    def __str__(self):
        """ Gives human-readable representation of the Customer Model """
        return f"{self.name} || {self.email} || {self.mobile_number}"


class Vehicle(models.Model):
    """ Model for vehicle table """

    YEARS_CHOICE = [(r, r) for r in range(1984, datetime.date.today().year+1)]
    CURRENT_YEAR = datetime.date.today().year

    year = models.IntegerField(choices=YEARS_CHOICE, default=CURRENT_YEAR)
    model = models.CharField(max_length=30)
    make = models.CharField(max_length=30)
    number = models.CharField(max_length=12)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                default=100000.00,
                                validators=[MinValueValidator(Decimal('30000.00'),
                                                              message="Values below 30000 are not permitted.")])

    def __str__(self):
        """ Gives human-readable representation of the Vehicle Model """
        return f"{self.number} || {self.year} || {self.price}"


class CoverageInfo(models.Model):
    """ Model for coverageinfo table which has details of coverages"""
    name = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        """ Gives human-readable representation of the CoverageInfo Model """
        return f"{self.name}"


class Quotation(models.Model):
    """ Model for quoations table """
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE)
    coverage = models.ManyToManyField(CoverageInfo)
    email_preference = models.BooleanField(default=False)
    quote_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.0)
