# Generated by Django 3.2.4 on 2021-06-09 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=25)),
                ('position', models.CharField(max_length=2)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fanta_soccer_app.team')),
            ],
        ),
    ]
