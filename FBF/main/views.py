from django.shortcuts import render
from django.views.generic import ListView
from .models import TeamPerson


def index(request):
    return render(request, 'main/index.html')


def about(requset):
    return render(requset, 'main/about.html')


def team(request):

    team = TeamPerson.objects.all()
    context = {
        'team': team
    }

    return render(request, 'main/team.html', context)

