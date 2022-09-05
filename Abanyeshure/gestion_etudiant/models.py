from django.db import models

# Create your models here.
genre = [("M", "Masculin"), ("F", "Feminin")]


class Etudiant(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=32)
    prenom = models.CharField(max_length=32)
    date_naissance = models.DateField()
    faculte = models.CharField(max_length=25)
    genre_etudiant = models.CharField(choices=genre, max_length=10)
