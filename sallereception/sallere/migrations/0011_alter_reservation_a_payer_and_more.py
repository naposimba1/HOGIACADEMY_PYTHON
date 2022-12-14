# Generated by Django 4.1 on 2022-08-27 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sallere', '0010_alter_reservation_a_payer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='a_payer',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='type_decor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='sallere.type_decor'),
        ),
    ]
