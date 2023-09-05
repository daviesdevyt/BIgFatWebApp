from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, HttpResponse, redirect
from django.http import JsonResponse
from django.contrib import messages
from utils.helpers import filter_objects
from .models import CartProduct, News, CC, Fullz, Dumps, Logs, Guides, Services, Order
from rest_framework.pagination import DjangoPaginator
from utils.cc_checker import cc_checker


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
            i = item.get_data
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
        purchases.append(item.get_data)
    return render(request, "base/purchases.html", {"purchases": purchases})

@login_required
def support(request):
    return render(request, 'base/support.html')


@login_required
def cc(request):
    attrs = ["base__name", "country", "state"]
    unique, filters = filter_objects(request, CC, attrs, "cc")
    f = {}
    for var, value in request.GET.items():
        if var in ["DOB", "ssn", "phone_number", "email"]:
            if value == "true":
                value = True
            if value == "false":
                value = False
            f[f"{var}__isnull"] = value
    if request.GET.get("cc"):
        filters["cc__startswith"] = request.GET.get("cc")
    paginator = DjangoPaginator(CC.objects.filter(purchased=False, **filters).order_by("date_created").exclude(**f), 10)
    return render(request, "base/cc.html", {"ccs": paginator.get_page(request.GET.get("page", 1)),
                                            "filters": unique, "attrs": attrs, "paginator": paginator})


@login_required
def fullz(request):
    attrs = ["category", "country", "state"]
    unique, filters = filter_objects(request, Fullz, attrs, "fullz")
    paginator = DjangoPaginator(Fullz.objects.filter(purchased=False, **filters).order_by("date_created"), 10)
    return render(request, "base/fullz.html",
                  {"fullzz": paginator.get_page(request.GET.get("page", 1)),
                   "filters": unique, "attrs": attrs, "paginator": paginator})


@login_required
def dumps(request):
    attrs = ["cc_type", "code", "country", "bank"]
    unique, filters = filter_objects(request, Dumps, attrs, "dumps")
    if request.GET.get("dumps"):
        filters["bin__startswith"] = request.GET.get("dumps")
    paginator = DjangoPaginator(Dumps.objects.filter(purchased=False, **filters).order_by("date_created"), 10)
    return render(request, "base/dumps.html", {"dumps": paginator.get_page(request.GET.get("page", 1)),
                                               "filters": unique, "attrs": attrs, "paginator": paginator})


@login_required
def logs(request, title):
    if title not in ["logs", "guides", "services"]:
        return HttpResponse(status=404)
    classes = {"logs": Logs, "guides": Guides, "services": Services}
    attrs = ["category"]
    unique, filters = filter_objects(request, classes[title], attrs, title.lower())
    paginator = DjangoPaginator(classes[title].objects.filter(purchased=False, **filters).order_by("date_created"), 10)
    return render(request, "base/logs.html",
                  {"data": paginator.get_page(request.GET.get("page", 1)), "name": title,
                   "filters": unique, "attrs": attrs, "paginator": paginator})


@login_required
def cart(request):
    cart = list()
    total = 0
    for item in CartProduct.objects.filter(user=request.user):
        i = item.get_data
        if i:
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
            i = item.get_data
            if i:
                total += i.price
                orders.append(Order(product=item.product, product_id=item.product_id, user=request.user))
        if total > request.user.balance:
            messages.error(request, "Insufficient balance")
            return redirect("cart")
        request.user.balance -= total
        request.user.save()
        Order.objects.bulk_create(orders)
        empty_cart(request)
    return redirect("purchases")


def purchases(request):
    purchases = list()
    for item in Order.objects.filter(user=request.user).order_by("-date_created"):
        i = item.get_data
        if i:
            purchases.append(i)
    return render(request, "base/purchases.html", {"purchases": purchases})

@login_required
def cc_checker_view(request, product_id):
    product = get_object_or_404(CC, id=product_id)
    if product.purchased:
        CartProduct.objects.filter(product_id=product_id, user=request.user).delete()
        return JsonResponse({"message":"Product has been bought", "code":400}, safe=False)
    
    response = cc_checker(product.cc, product.month, product.year, product.cvv)
    if response:
        status = response.get("status" ,"")
        status = "valid" if status.find("LIVE") != -1 else "decline"
        return JsonResponse({"status": status, "code": 200}, safe=False)
    return JsonResponse({"message":"Service tempoarily unavailable", "code":400}, safe=False)
