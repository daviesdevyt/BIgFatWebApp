from django.shortcuts import render

from django.contrib.auth.decorators import login_required

# Create your views here.
def news(request):
    return render(request, 'base/news.html')


