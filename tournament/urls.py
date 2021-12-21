from django.urls import path
from .views import CreateTournament, TournamentList, tournament_details_view

app_name = 'tournament'

urlpatterns = [
    path('', CreateTournament.as_view(), name='start_tournament'),
    # path('', create_tournament_view, name='start_tournament'),
    path('leagues/', TournamentList.as_view(), name='tournament_list'),
    path('league/<int:league_id>/', tournament_details_view, name='league_details'),
]