from django.db import models

# Create your models here.


class Eleve(models.Model):
    id = models.BigAutoField(primary_key=True)
    matricule = models.CharField(max_length=10)
    nom = models.CharField(max_length=32)
    prenom = models.CharField(max_length=32)
    datenaissance = models.DateField()
    sexe = models.CharField(max_length=2)
    autres = models.TextField()

    def __str__(self):
        return f"{self.nom} {self.prenom} {self.datenaissance} {self.matricule} {self.autres}"


class Cours(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=64)
    volHoraire = models.PositiveIntegerField()
    prof = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.nom} {self.prof} {self.volHoraire}"


class Point(models.Model):
    id = models.BigAutoField(primary_key=True)
    # uhanague eleve namanot yiw bica bijana
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE)
    # uhanague cours hagend io cours gusa
    cours = models.ForeignKey(Cours, null=True, on_delete=models.SET_NULL)
    points = models.IntegerField()

    def __str__(self):
        return f"{self.eleve} {self.cours.nom} {self.points}/20"
