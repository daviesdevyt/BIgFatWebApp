from django.shortcuts import render, HttpResponse

from .models import News, CC, Fullz, Dumps, Logs, Guides, Services
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
    return render(request, "base/fullz.html", {"fullzz": Fullz.objects.order_by("date_created")})

def dumps(request):
    return render(request, "base/dumps.html", {"dumps": Dumps.objects.order_by("date_created")})

def logs(request, title):
    if title not in ["logs", "guides", "services"]:
        return HttpResponse(status=404)
    classes = {"logs": Logs, "guides": Guides, "services": Services}
    return render(request, "base/logs.html", {"data": classes[title].objects.order_by("date_created"), "name": title})


