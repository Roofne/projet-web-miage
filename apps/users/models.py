import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class beneficiaire(models.Model):
    Nom=models.CharField(max_length=255)
    prenom=models.CharField(max_length=255)
    mail=models.CharField(max_length=255)
    telephone=models.CharField(max_length=255)
    postale=models.CharField(max_length=255)
    nb_parts=models.CharField(max_length=255)
    mot_mairie=models.BooleanField(default=False)
    carte_donnee=models.BooleanField(default=False)
    presence_aux_distributions=models.BooleanField(default=False)
    champ_remarque=models.TextField(max_length=255)

    # Définition des méthodes
    def __str__(self):
        return "1"
