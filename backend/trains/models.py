from django.db import models

class Train(models.Model):
    name = models.CharField(max_length=200)
    fare = models.DecimalField(max_digits=10, decimal_places=2)
    total_seats = models.PositiveIntegerField(default=100)
    available_seats = models.PositiveIntegerField(default=100)

    def __str__(self):
        return f"{self.name} ({self.available_seats}/{self.total_seats})"
