from django import forms
from django.core.exceptions import ValidationError
from fanta_soccer_app.models import Squad, League


class CreateTournamentForm(forms.ModelForm):
    class Meta:
        model = League
        fields = ['league_name', 'number_of_squads']

    # TYPES = [('RR', 'Round Robin'), ('El', 'Elimination')]
    type_of_tournament = forms.ChoiceField(choices=League.TYPES, widget=forms.RadioSelect())
    selection = forms.ModelMultipleChoiceField(queryset=Squad.objects.all(),
                                               widget=forms.CheckboxSelectMultiple,
                                               )

    def clean(self):
        cleaned_data = super(CreateTournamentForm, self).clean()
        nos = cleaned_data.get('number_of_squads')
        selected = cleaned_data.get('selection').count()
        # validate the form through cross-fields values
        if nos != selected:
            raise ValidationError(
                'this is not the correct number of squads'
            )
        return cleaned_data

