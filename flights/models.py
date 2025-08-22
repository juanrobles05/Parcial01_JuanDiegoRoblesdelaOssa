from django.db import models
from django.core.validators import MinValueValidator

class Flight(models.Model):
    NATIONAL = 'Nacional'
    INTERNATIONAL = 'Internacional'
    TYPE_CHOICES = [
        (NATIONAL, 'Nacional'),
        (INTERNATIONAL, 'Internacional'),
    ]

    name = models.CharField(max_length=120)
    flight_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                validators=[MinValueValidator(0)])

    class Meta:
        ordering = ['price']

    def __str__(self):
        return f'{self.name} ({self.flight_type}) - ${self.price}'