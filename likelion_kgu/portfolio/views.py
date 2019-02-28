from django.shortcuts import render
from portfolio.models import Portfolio
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def main(request):
    if request.GET.get('number'):
        portfolio = Portfolio.objects.filter(likelion__group_number = request.GET.get('number')).order_by('-id')
    else:
        portfolio = Portfolio.objects.filter(likelion__group_number = 7).order_by('-id')
    paginator = Paginator(portfolio, 3) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    context = {'contacts': contacts}
    return render(request, 'portfolio/main.html', context)