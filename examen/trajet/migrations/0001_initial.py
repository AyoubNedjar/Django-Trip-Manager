# Generated by Django 5.0.6 on 2024-06-03 15:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, verbose_name='Nom')),
                ('prenom', models.CharField(max_length=100, verbose_name='Prénom')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('telephone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Téléphone')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Conducteur',
            fields=[
                ('nom', models.CharField(max_length=100, verbose_name='Nom')),
                ('prenom', models.CharField(max_length=100, verbose_name='Prénom')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('telephone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Téléphone')),
                ('matricule', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Matricule')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Trajet',
            fields=[
                ('code', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Code Trajet')),
                ('description', models.TextField(verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='Troncon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('villeDep', models.CharField(max_length=100, verbose_name='Ville de départ')),
                ('villeDest', models.CharField(max_length=100, verbose_name='Ville de destination')),
                ('distance', models.FloatField(verbose_name='Distance')),
                ('prix', models.FloatField(verbose_name='Prix')),
            ],
        ),
        migrations.CreateModel(
            name='ClientSpecial',
            fields=[
                ('client_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='trajet.client')),
                ('reduction', models.SmallIntegerField(verbose_name='Réduction')),
            ],
            options={
                'abstract': False,
            },
            bases=('trajet.client',),
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateReserve', models.DateTimeField(verbose_name='Date de réservation')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trajet.client', verbose_name='Client')),
            ],
        ),
        migrations.CreateModel(
            name='TrajectEffect',
            fields=[
                ('effectTrajet', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Effect Trajet')),
                ('dateDepart', models.DateTimeField(verbose_name='Date de départ')),
                ('clients', models.ManyToManyField(related_name='reservations', through='trajet.Reservation', to='trajet.client', verbose_name='Clients')),
                ('conducteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trajet.conducteur', verbose_name='Conducteur')),
                ('trajet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trajet.trajet', verbose_name='Trajet associé')),
            ],
        ),
        migrations.AddField(
            model_name='reservation',
            name='trajectEffect',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trajet.trajecteffect', verbose_name='Traject Effectué'),
        ),
        migrations.CreateModel(
            name='TrRegulier',
            fields=[
                ('trajet_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='trajet.trajet')),
                ('jour', models.CharField(choices=[('Q', 'Quotidien'), ('S', 'Hebdomadaire'), ('W', 'Weekend')], max_length=1, verbose_name='Fréquence')),
            ],
            bases=('trajet.trajet',),
        ),
        migrations.CreateModel(
            name='TrSpecial',
            fields=[
                ('trajet_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='trajet.trajet')),
                ('evenement', models.CharField(max_length=100, verbose_name='Événement')),
                ('datePrev', models.DateField(verbose_name='Date Prévue')),
            ],
            bases=('trajet.trajet',),
        ),
        migrations.AddField(
            model_name='trajet',
            name='troncons',
            field=models.ManyToManyField(related_name='trajets', to='trajet.troncon', verbose_name='Tronçons'),
        ),
    ]
