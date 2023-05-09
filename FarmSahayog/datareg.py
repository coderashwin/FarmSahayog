from django.db import models

class Registration(models.Model):
    district = models.CharField(max_length=50)
    tehsil = models.CharField(max_length=50)
    village = models.CharField(max_length=50)
    khasra = models.CharField(max_length=50)
