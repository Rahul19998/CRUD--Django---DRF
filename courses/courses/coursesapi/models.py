from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

# Create your models here.


class Courses(models.Model):
    # id = models.IntegerField(primary_key=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=255)
    image_path = models.CharField(max_length=100, null=True, blank=True)
    on_discount = models.BooleanField(null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    title = models.CharField(max_length=100, null=False,
                             validators=[MinValueValidator(5)])
    # title = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.title
