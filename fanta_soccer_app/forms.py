from django import forms
from .models import Squad, AvailablePlayer, get_user_model
from django.contrib.auth.decorators import login_required


class SquadForm(forms.ModelForm):
    class Meta:
        model = Squad
        fields = ['squad_name']
        labels = {'Squad Name': ''}


class AddPlayerToSquadForm(forms.Form):
    player_to_squad = forms.ModelChoiceField(queryset=AvailablePlayer.objects.all().
                                             filter(squad=None))


class AddSquadToPlayerForm(forms.ModelForm):
    class Meta:
        model = Squad
        fields = ['squad_name']

    # overriding the constructor to pass the user, and show only squads of that user
    def __init__(self, user, *args, **kwargs):
        super(AddSquadToPlayerForm, self).__init__(*args, **kwargs)
        self.fields['squad_name'] = forms.ModelChoiceField(queryset=Squad.objects.filter(manager=user))
