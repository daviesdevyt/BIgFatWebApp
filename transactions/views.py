from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from authentication.models import User
from utils.constants import TransactionStatus
from utils.oxapay import Oxapay
from .models import Transaction
# Create your views here.


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
            Transaction.objects.create(amount=amt, track_id=res["trackId"], user=request.user)
            User.objects.filter(id=request.user.id).update(pay_link=res["payLink"])
        except:
            amt = request.COOKIES.get('amt')
    else:
        amt = request.COOKIES.get('amt')
        if not amt:
            amt = 100
    trackId = request.GET.get("trackId")
    status = request.GET.get("status")
    if trackId and status:
        verify_tx(request)
    response = render(request, 'transactions/add-money.html', {"amt": amt})
    response.set_cookie("amt", amt)
    return response


def verify_tx(request):
    if request.method == "GET":
        trackId = request.GET.get("trackId")
        status = request.GET.get("status")
        tx = Transaction.objects.filter(track_id=trackId).first()
        if tx and tx.status == TransactionStatus.completed:
            return HttpResponse(status=200)
        if status == "1":
            tx = Oxapay().get_transaction(trackId)
            if tx["status"] == 1:
                user = User.objects.filter(username=tx["description"]).first()
                user.pay_link = None
                Transaction.objects.filter(track_id=trackId).update(status=TransactionStatus.completed)
                user.balance += tx["amount"]
                user.save()
    return HttpResponse(status=200)
