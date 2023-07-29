from django.shortcuts import render

from .models import News
# Create your views here.
def news(request):
    return render(request, 'base/news.html', {"news": News.objects.order_by("-pub_date")})

def wallet(request):
    return render(request, 'base/add money.html')

def support(request):
    return render(request, 'base/support.html')

