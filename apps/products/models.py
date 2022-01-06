import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Produits(models.Model):
    # Définition des attributs
    nom = models.CharField(max_length=255)
    qty = models.CharField(max_length=255)
    category = models.CharField(max_length=255)

    # Définition des méthodes
    def __str__(self):
        return "1"

    # Définition des méthodes
    def __str__(self):
        return "1"
