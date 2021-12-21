"""Defining URL patterns for fanta_soccer_app"""

from django.urls import path

from . import views

app_name = 'fanta_soccer_app'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page to show all the Squads
    path('squads/', views.squads, name='squads'),
    # Team's list of players
    path('squads/<int:squad_id>/', views.squad, name='squad'),
    # Add new Team
    path('new_squad/', views.new_squad, name='new_squad'),
    # Add new Player to a Squad
    path('add_player/<int:squad_id>/', views.add_player_to_squad, name='add_player'),
    # Page to show allavailable players
    path('playerslist/', views.available_players, name='available_players'),
    # Player Info
    path('playerslist/<int:player_id>/', views.player_detail, name='player_detail'),
    # Add a Squad to a Player
    path('add_squad/<int:player_id>/', views.add_squad_to_player, name='add_squad'),
    # User's profile page
    path('profile/', views.profile_view, name='profile'),
]