# Generated by Django 4.1 on 2022-09-01 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacie_app', '0005_alter_client_sexe_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='date_expiration',
            field=models.DateField(default=1),
            preserve_default=False,
        ),
    ]
