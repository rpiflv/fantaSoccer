# Generated by Django 3.2.7 on 2021-10-27 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fanta_soccer_app', '0022_rename_type_league_type_of_tournament'),
    ]

    operations = [
        migrations.AlterField(
            model_name='league',
            name='type_of_tournament',
            field=models.CharField(blank=True, choices=[('RR', 'Round Robin'), ('EL', 'Elimination')], max_length=25, null=True),
        ),
    ]