# Generated by Django 3.2.7 on 2021-10-26 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fanta_soccer_app', '0018_auto_20211017_1145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='squad',
            name='tournament_in',
        ),
        migrations.AddField(
            model_name='league',
            name='squads',
            field=models.ManyToManyField(to='fanta_soccer_app.Squad'),
        ),
        migrations.AddField(
            model_name='league',
            name='type',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
