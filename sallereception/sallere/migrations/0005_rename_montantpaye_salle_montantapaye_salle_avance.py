# Generated by Django 4.1 on 2022-08-26 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sallere', '0004_rename_nom_client_salle_nomclient_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salle',
            old_name='montantpaye',
            new_name='montantapaye',
        ),
        migrations.AddField(
            model_name='salle',
            name='avance',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
