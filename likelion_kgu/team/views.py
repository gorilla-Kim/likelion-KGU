from django.shortcuts import render
from likelion.models import likelion
from .models import Team

# Create your views here.

def team(request):
    teams = Team.objects.all()
    likelions = likelion.objects.all().order_by('-group_number')
    context = {"teams":teams , "likelions":likelions}
    return render(request, "team/team.html", context)