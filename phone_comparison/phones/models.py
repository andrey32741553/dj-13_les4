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
