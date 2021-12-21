from django.db import models

from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator


class Squad(models.Model):
    """template for each Team in the League"""
    squad_name = models.CharField(max_length=20)
    manager = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.squad_name

    def get_absolute_url(self):
        return reverse('squad', args=[str(self.id)])


class League(models.Model):
    league_name = models.CharField(max_length=22)
    number_of_squads = models.IntegerField(default=4, validators=[MaxValueValidator(10), MinValueValidator(4)])
    TYPES = [('RR', 'Round Robin'), ('EL', 'Elimination')]
    type_of_tournament = models.CharField(max_length=25, choices=TYPES, null=True, blank=True)
    squads = models.ManyToManyField(Squad, related_name='leagues')

    def __str__(self):
        return self.league_name


class AvailablePlayer(models.Model):
    player_name = models.CharField(max_length=25)
    team_real = models.CharField(max_length=5)
    position = models.CharField(max_length=5)
    squad = models.ForeignKey(Squad, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.player_name


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), null=True, on_delete=models.CASCADE)
    motto = models.TextField(max_length=220)

    def __str__(self):
        return str(self.user)
