from django.shortcuts import render
from portfolio.models import Portfolio
from team.models import Team
from .models import likelion
# Create your views here.
def home(request):
    portfolios = Portfolio.objects.all().order_by('-id')
    portfolio = []
    # 최신 6개의 포트폴리오만 띄우기 위함입니다.
    for i in range(0,6):
        try:
            portfolio.append(portfolios[i])
        except:
            continue
    print(portfolio)

    teams = Team.objects.all()
    likelions = likelion.objects.all().order_by("-group_number")
    likelion_new = likelions[0]

    context = {'portfolio':portfolio, "teams":teams, "likelion_new":likelion_new}
    return render(request, 'likelion/home.html', context)