# Generated by Django 4.1 on 2022-08-31 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacie_app', '0003_rename_cni_client_nom_client_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnel',
            name='sexe',
            field=models.CharField(choices=[('M', 'Masculin'), ('F', 'Feminin')], max_length=10),
        ),
    ]