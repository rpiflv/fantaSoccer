from django.shortcuts import render, redirect
from .models import Squad, AvailablePlayer, Profile
from .forms import SquadForm, AddPlayerToSquadForm, AddSquadToPlayerForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory


def index(request):
    return render(request, 'fanta_soccer_app/index.html')


def squad(request, squad_id):
    """Show list of players for each squad"""
    squad = Squad.objects.get(id=squad_id)
    players = squad.availableplayer_set.all()
    context = {'squad': squad, 'players': players}
    return render(request, 'fanta_soccer_app/squad.html', context)


def squads(request):
    """Show all Squads"""
    squads = Squad.objects.all()
    context = {'squads': squads}
    return render(request, 'fanta_soccer_app/squads.html', context)

@login_required()
def new_squad(request):
    if request.method != 'POST':
        form = SquadForm()
    else:
        form = SquadForm(data=request.POST)
        if form.is_valid():
            n_squad = form.save(commit=False)
            n_squad.manager = get_user_model().objects.get(username=request.user)
            n_squad.save()
            return redirect('fanta_soccer_app:squads')
    context = {'form': form}
    return render(request, 'fanta_soccer_app/new_squad.html', context)


# @login_required()
# def edit_squad(request):
#     if request.method != 'POST':
#


@login_required()
def add_player_to_squad(request, squad_id):
    squad = Squad.objects.get(id=squad_id)
    if request.method == "POST" and request.user == squad.manager:
        form = AddPlayerToSquadForm(request.POST)

        if form.is_valid():
            player_to_sign = form.cleaned_data['player_to_squad']
            player_to_sign.squad = squad
            player_to_sign.save()
            return redirect('fanta_soccer_app:squad', squad_id=squad_id)
    else:
        form = AddPlayerToSquadForm()
    context = {"squad": squad, "form": form}
    return render(request, 'fanta_soccer_app/add_player.html', context)


def available_players(request):
# shows the list of all available players from table
    available_players = AvailablePlayer.objects.all()
    context = {'available_players': available_players}
    return render(request, 'fanta_soccer_app/playerslist.html', context)


def player_detail(request, player_id):
    player_info = AvailablePlayer.objects.get(id=player_id)
    context = {'player_info': player_info}
    return render(request, 'fanta_soccer_app/player_detail.html', context)

@login_required()
def add_squad_to_player(request, player_id):
    player = AvailablePlayer.objects.get(id=player_id)
    if request.method == "POST":
        form = AddSquadToPlayerForm(request.user, request.POST)
        if form.is_valid():
            squad_to_join = form.save(commit=False)
            player.squad = squad_to_join
            squad_to_join.save()
            player.save()
            return redirect('fanta_soccer_app:player_detail', player_id=player_id)
    else:
        form = AddSquadToPlayerForm(request.user, request.POST)
        # form.squad_to_player.queryset = Squad.objects.filter(manager_id=request.user)
    context = {"player": player, "form": form}
    return render(request, 'fanta_soccer_app/add_squad.html', context)

@login_required()
def profile_view(request):
    profile_id = request.user
    print(profile_id)
    squads_profile = profile_id.squad_set.all()
    print(squads_profile)
    return render(request, 'fanta_soccer_app/profile.html', {'squads_profile': squads_profile})
