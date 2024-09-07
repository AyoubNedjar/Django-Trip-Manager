from django.db import models
from django.utils.translation import gettext_lazy as _

class Personne(models.Model):
    nom = models.CharField(max_length=100, verbose_name='Nom')
    prenom = models.CharField(max_length=100, verbose_name='Prénom')
    email = models.EmailField(blank=True, null=True, verbose_name='Email')
    telephone = models.CharField(max_length=15, blank=True, null=True, verbose_name='Téléphone')

    class Meta:
        #on a utiliser un heritage total d'ou le abstract et 
        abstract = True

class Conducteur(Personne):
    matricule = models.CharField(max_length=10, primary_key=True, verbose_name='Matricule')

class Client(Personne):
    pass

class ClientSpecial(Client):
    reduction = models.SmallIntegerField(verbose_name='Réduction')

class Trajet(models.Model):
    code = models.CharField(max_length=20, primary_key=True, verbose_name='Code Trajet')
    description = models.TextField(verbose_name='Description')
    troncons = models.ManyToManyField('Troncon', related_name='trajets', verbose_name='Tronçons')

class Frequence(models.TextChoices):
    QUOTIDIEN = 'Q', _('Quotidien')
    HEBDOMADAIRE = 'S', _('Hebdomadaire')
    WEEKEND = 'W', _('Weekend')

class TrRegulier(Trajet):
    jour = models.CharField(max_length=1, choices=Frequence.choices, verbose_name='Fréquence')

class TrSpecial(Trajet):
    evenement = models.CharField(max_length=100, verbose_name='Événement')
    datePrev = models.DateField(verbose_name='Date Prévue')

class TrajectEffect(models.Model):
    effectTrajet = models.CharField(max_length=50, primary_key=True, verbose_name='Effect Trajet')
    dateDepart = models.DateTimeField(verbose_name='Date de départ')
    conducteur = models.ForeignKey(Conducteur, on_delete=models.CASCADE, verbose_name='Conducteur')
    trajet = models.ForeignKey(Trajet, on_delete=models.CASCADE, verbose_name='Trajet associé')
    clients = models.ManyToManyField(Client, through='Reservation', related_name='reservations', verbose_name='Clients')

class Reservation(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Client')
    trajectEffect = models.ForeignKey(TrajectEffect, on_delete=models.CASCADE, verbose_name='Traject Effectué')
    dateReserve = models.DateTimeField(verbose_name='Date de réservation')

class Troncon(models.Model):
    villeDep = models.CharField(max_length=100, verbose_name='Ville de départ')
    villeDest = models.CharField(max_length=100, verbose_name='Ville de destination')
    distance = models.FloatField(verbose_name='Distance')
    prix = models.FloatField(verbose_name='Prix')
