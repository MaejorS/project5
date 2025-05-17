from django.db import models

class Product(models.Model):
    BRAND_CHOICES = [
        ('apple', 'Apple'),
        ('samsung', 'Samsung'),
    ]

    GRADE_CHOICES = [
        ('A', 'Grade A'),
        ('B', 'Grade B'),
    ]

    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=20, choices=BRAND_CHOICES)
    grade = models.CharField(max_length=1, choices=GRADE_CHOICES)
    storage_gb = models.PositiveIntegerField(help_text="Enter storage in GB as an integer (e.g. 128)")
    camera_megapixels = models.DecimalField(max_digits=4, decimal_places=1)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name