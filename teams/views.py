from django.shortcuts import render

from .models import Team


def list_team_members(request):
    members = Team.objects.all()
    context = {
        'members': members,
    }
    return render(request, 'teams/list.html', context)
