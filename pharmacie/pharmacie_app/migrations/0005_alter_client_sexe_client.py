# Generated by Django 4.1 on 2022-08-31 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacie_app', '0004_alter_personnel_sexe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='sexe_client',
            field=models.CharField(choices=[('M', 'Masculin'), ('F', 'Feminin')], max_length=10),
        ),
    ]
