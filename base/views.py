from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from utils.helpers import filter_objects
from .models import CartProduct, News, CC, Fullz, Dumps, Logs, Guides, Services, Order
from rest_framework.pagination import DjangoPaginator


# Create your views here.

@login_required
def news(request):
    return render(request, 'base/news.html', {"news": News.objects.order_by("-pub_date")})

@login_required
def checkout(request):
    cart = CartProduct.objects.filter(user=request.user)
    if len(cart) > 0:
        orders = []
        total = 0
        for item in cart:
            i = item.get_data()
            total += i.price
            orders.append(Order(product=item.product, product_id=item.product_id, user=request.user))
        if total > request.user.balance:
            messages.error(request, "Insufficient balance")
            return redirect("cart")
        Order.objects.bulk_create(orders)
        empty_cart(request)
    return redirect("purchases")


def purchases(request):
    purchases = list()
    for item in Order.objects.filter(user=request.user):
        purchases.append(item.get_data())
    return render(request, "base/purchases.html", {"purchases": purchases})

@login_required
def support(request):
    return render(request, 'base/support.html')


@login_required
def cc(request):
    attrs = ["base", "country", "state"]
    unique, filters = filter_objects(request, CC, attrs, "cc")
    paginator = DjangoPaginator(CC.objects.filter(purchased=False, **filters).order_by("date_created"), 20)
    return render(request, "base/cc.html", {"ccs": paginator.get_page(request.GET.get("page", 1)),
                                            "filters": unique, "attrs": attrs, "paginator": paginator})


@login_required
def fullz(request):
    attrs = ["category", "country", "state"]
    unique, filters = filter_objects(request, Fullz, attrs, "fullz")
    paginator = DjangoPaginator(Fullz.objects.filter(purchased=False, **filters).order_by("date_created"), 20)
    return render(request, "base/fullz.html",
                  {"fullzz": paginator.get_page(request.GET.get("page", 1)),
                   "filters": unique, "attrs": attrs, "paginator": paginator})


@login_required
def dumps(request):
    attrs = ["cc_type", "code", "country", "bank"]
    unique, filters = filter_objects(request, Dumps, attrs, "dumps")
    paginator = DjangoPaginator(Dumps.objects.filter(purchased=False, **filters).order_by("date_created"), 20)
    return render(request, "base/dumps.html", {"dumps": paginator.get_page(request.GET.get("page", 1)),
                                               "filters": unique, "attrs": attrs, "paginator": paginator})


@login_required
def logs(request, title):
    if title not in ["logs", "guides", "services"]:
        return HttpResponse(status=404)
    classes = {"logs": Logs, "guides": Guides, "services": Services}
    attrs = ["category"]
    unique, filters = filter_objects(request, classes[title], attrs, title.lower())
    paginator = DjangoPaginator(classes[title].objects.filter(purchased=False, **filters).order_by("date_created"), 20)
    return render(request, "base/logs.html",
                  {"data": paginator.get_page(request.GET.get("page", 1)), "name": title,
                   "filters": unique, "attrs": attrs, "paginator": paginator})


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
    return HttpResponse(request.user.cart.count(), status=200)


@login_required
def empty_cart(request):
    CartProduct.objects.filter(user=request.user).delete()
    return redirect("cart")


@login_required
def checkout(request):
    cart = CartProduct.objects.filter(user=request.user)
    if len(cart) > 0:
        orders = []
        total = 0
        for item in cart:
            i = item.get_data()
            total += i.price
            orders.append(Order(product=item.product, product_id=item.product_id, user=request.user))
        if total > request.user.balance:
            messages.error(request, "Insufficient balance")
            return redirect("cart")
        Order.objects.bulk_create(orders)
        empty_cart(request)
    return redirect("purchases")


def purchases(request):
    purchases = list()
    for item in Order.objects.filter(user=request.user):
        purchases.append(item.get_data())
    return render(request, "base/purchases.html", {"purchases": purchases})
