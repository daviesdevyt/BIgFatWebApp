from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required

from .models import CartProduct, News, CC, Fullz, Dumps, Logs, Guides, Services
# Create your views here.
@login_required
def news(request):
    return render(request, 'base/news.html', {"news": News.objects.order_by("-pub_date")})
@login_required
def wallet(request):
    return render(request, 'base/add money.html')
@login_required
def support(request):
    return render(request, 'base/support.html')
@login_required
def cc(request):
    return render(request, "base/cc.html", {"ccs": CC.objects.order_by("date_created")})
@login_required
def fullz(request):
    return render(request, "base/fullz.html", {"fullzz": Fullz.objects.order_by("date_created")})
@login_required
def dumps(request):
    return render(request, "base/dumps.html", {"dumps": Dumps.objects.order_by("date_created")})
@login_required
def logs(request, title):
    if title not in ["logs", "guides", "services"]:
        return HttpResponse(status=404)
    classes = {"logs": Logs, "guides": Guides, "services": Services}
    return render(request, "base/logs.html", {"data": classes[title].objects.order_by("date_created"), "name": title})

@login_required
def cart(request):
    cart = list()
    total = 0
    for item in CartProduct.objects.filter(user=request.user):
        i = item.get_data()
        total += i.price
        cart.append(i)
    return render(request, "base/cart.html", {"total": total, "cart": cart})

@login_required
def delete_cart(request, prod_id):
    p = CartProduct.objects.filter(id=prod_id)
    if p:
        p.delete()
    return redirect("cart")

@login_required
def add_cart(request, type, prod_id):
    CartProduct.objects.create(product=type, product_id=prod_id, user=request.user)
    return HttpResponse(status=200)

@login_required
def empty_cart(request):
    CartProduct.objects.filter(user=request.user).delete()
    return redirect("cart")
