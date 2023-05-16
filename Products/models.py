from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    image = models.URLField()

    def __str__(self):
        return self.name