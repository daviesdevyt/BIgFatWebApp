from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect

from authentication.models import User
from utils.oxapay import Oxapay
from .models import CartProduct, News, CC, Fullz, Dumps, Logs, Guides, Services, Order


# Create your views here.

@login_required
def news(request):
    return render(request, 'base/news.html', {"news": News.objects.order_by("-pub_date")})


@login_required
def wallet(request):
    if request.method == "POST":
        amt = request.POST.get("amt")
        if not amt:
            return HttpResponse(status=400)
        try:
            amt = float(amt)
            base_url = "https://" + request.get_host()
            res = Oxapay().payment_request(amt, base_url + "/verify", returnUrl=base_url + "/transactions",
                                           description=request.user.username)
            request.user.pay_link = res["payLink"]
            User.objects.filter(id=request.user.id).update(pay_link=res["payLink"])
        except:
            amt = request.COOKIES.get('amt')
    else:
        amt = request.COOKIES.get('amt')
        if not amt:
            amt = 100
    response = render(request, 'base/add-money.html', {"amt": amt})
    response.set_cookie("amt", amt)
    return response


@login_required
def support(request):
    return render(request, 'base/support.html')


@login_required
def cc(request):
    return render(request, "base/cc.html", {"ccs": CC.objects.filter(purchased=False).order_by("date_created")})


@login_required
def fullz(request):
    return render(request, "base/fullz.html",
                  {"fullzz": Fullz.objects.filter(purchased=False).order_by("date_created")})


@login_required
def dumps(request):
    return render(request, "base/dumps.html", {"dumps": Dumps.objects.filter(purchased=False).order_by("date_created")})


@login_required
def logs(request, title):
    if title not in ["logs", "guides", "services"]:
        return HttpResponse(status=404)
    classes = {"logs": Logs, "guides": Guides, "services": Services}
    return render(request, "base/logs.html",
                  {"data": classes[title].objects.filter(purchased=False).order_by("date_created"), "name": title})


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


def verify_tx(request):
    if request.method == "GET":
        trackId = request.GET.get("trackId")
        status = request.GET.get("status")
        if status == "1":
            tx = Oxapay().get_transaction(trackId)
            if tx["status"] == 1:
                user = User.objects.filter(username=tx["description"]).first()
                user.balance += tx["amount"]
                user.save()
    return HttpResponse(status=200)


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
            # TODO: Alert no enough balance
            return redirect("cart")
        Order.objects.bulk_create(orders)
        empty_cart(request)
    return redirect("purchases")


def purchases(request):
    purchases = list()
    for item in Order.objects.filter(user=request.user):
        purchases.append(item.get_data())
    return render(request, "base/purchases.html", {"purchases": purchases})
