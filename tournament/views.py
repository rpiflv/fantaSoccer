from django.shortcuts import render
from .forms import CreateTournamentForm
from fanta_soccer_app.models import League, Squad
from django.views.generic import ListView, FormView
from django.urls import reverse_lazy


class CreateTournament(FormView):
    model = League
    form_class = CreateTournamentForm
    template_name = 'tournament/start_tournament.html'
    success_url = reverse_lazy('tournament:tournament_list')

    def form_valid(self, form):
        s = form.save(commit=False)
        s.selection = form.cleaned_data['selection']
        l_instance = League()
        l_instance.type_of_tournament = form.cleaned_data['type_of_tournament']
        l_instance.league_name = form.cleaned_data['league_name']
        l_instance.save()
        squad_list = Squad.objects.filter(pk__in=s.selection)
        for squad in squad_list:
            squad.leagues.add(l_instance)
        return super(CreateTournament, self).form_valid(form)


class TournamentList(ListView):
    model = League
    template_name = 'tournament/list_tournament.html'
    context_object_name = 'leagues'


def tournament_details_view(request, league_id):
    league = League.objects.get(id=league_id)
    squads = league.squads.all()
    context = {'league': league, 'squads': squads}
    return render(request, 'tournament/league_details.html', context)
