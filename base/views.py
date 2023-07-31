from django.shortcuts import render

from .models import News, CC, Fullz
# Create your views here.
def news(request):
    return render(request, 'base/news.html', {"news": News.objects.order_by("-pub_date")})

def wallet(request):
    return render(request, 'base/add money.html')

def support(request):
    return render(request, 'base/support.html')

def cc(request):
    return render(request, "base/cc.html", {"ccs": CC.objects.order_by("date_created")})

def fullz(request):
    return render(request, "base/fullz.html", {"fullzs": Fullz.objects.order_by("date_created")})