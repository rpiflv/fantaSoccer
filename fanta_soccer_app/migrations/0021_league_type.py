# Generated by Django 3.2.7 on 2021-10-26 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fanta_soccer_app', '0020_remove_league_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='league',
            name='type',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
