from django.db import models

# Create your models here.


class Salle(models.Model):
    id = models.BigAutoField(primary_key=True)
    nomClient = models.CharField(max_length=32)
    prenomClient = models.CharField(max_length=32)
    phoneClient = models.CharField(max_length=32)
    # sexe = models.TextChoices("M", "F")
    #sexe = models.TextChoices("M", "F")
    nomfete = models.CharField(max_length=32)
    montantpaye = models.IntegerField()
    datedelafete = models.DateField()
    nombrejr = models.IntegerField()
    autres = models.TextField()

    def __str__(self):
        return f"{self.nomclient} {self.prenomclient} {self.sexe} {self.nomfete} {self.datedelafete} {self.nombrejr} {self.autres}"


class Salleadmin(admin.ModelAdmin):
    list_display = ('nomClient', 'prenomClient', 'phoneClient',
                    'nomfete', 'montantpaye', 'datedelafete', 'nombrejr')
    list_filter = ('nomClient')
