# Generated by Django 3.2.4 on 2021-07-20 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fanta_soccer_app', '0011_rename_available_player_availableplayer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Team',
            new_name='Squad',
        ),
        migrations.RenameField(
            model_name='squad',
            old_name='team_name',
            new_name='squad_name',
        ),
    ]
