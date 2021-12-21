from .models import Squad


def navbar_dropdown_squad_list(request):
    nav_dropdown_squads = Squad.objects.all()
    return {
        'nav_dropdown_squads': nav_dropdown_squads
    }