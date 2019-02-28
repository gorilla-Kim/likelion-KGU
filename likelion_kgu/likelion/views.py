from django.shortcuts import render
from portfolio.models import Portfolio
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
    context = {'portfolio':portfolio}
    return render(request, 'likelion/home.html', context)