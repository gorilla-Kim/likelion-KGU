from django.shortcuts import render

# Create your views here.
def main(request):
    context = {}
    portfolios = Portfolio.objects.all()
    print("**********")
    print(portfolios)
    return render(request, 'portfolio/main.html', context)