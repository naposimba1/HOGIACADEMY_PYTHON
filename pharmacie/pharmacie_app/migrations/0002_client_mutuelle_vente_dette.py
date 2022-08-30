# Generated by Django 4.1 on 2022-08-30 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacie_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nom_personnel', models.CharField(max_length=32)),
                ('prenom_personnel', models.CharField(max_length=32)),
                ('phone_personnel', models.CharField(max_length=32)),
                ('sexe', models.CharField(max_length=10)),
                ('cni', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Mutuelle',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nom_mutuelle', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Vente',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('valeur_total', models.IntegerField(default=0)),
                ('payer', models.IntegerField(default=0)),
                ('a_payer', models.IntegerField(default=0)),
                ('paid', models.BooleanField(default=True)),
                ('date_vente', models.DateTimeField(auto_now=True)),
                ('agence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacie_app.agence')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacie_app.client')),
                ('personnel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacie_app.personnel')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacie_app.produit')),
            ],
        ),
        migrations.CreateModel(
            name='Dette',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('date_paye', models.DateTimeField(blank=True, null=True)),
                ('vente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacie_app.vente')),
            ],
        ),
    ]
