from django.db import models


class Phone(models.Model):
    name = models.TextField()
    price = models.TextField()
    os = models.TextField()
    processor = models.TextField()
    display = models.TextField()
    resolution = models.TextField()
    built_in_memory = models.TextField()
    ram = models.TextField()
    special = models.ForeignKey(
        'SpecialProperties',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )


class SpecialProperties(models.Model):
    property_n1 = models.TextField()
    property_n2 = models.TextField()
