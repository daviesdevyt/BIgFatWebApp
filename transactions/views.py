from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from authentication.models import User
from utils.constants import TransactionStatus
from utils.coinbase import Coinbase
from utils.helpers import confirm_payment
from .models import Transaction
from django.conf import settings
from datetime import datetime
from django.shortcuts import get_object_or_404
from django.contrib import messages


# Create your views here.
coinbase = Coinbase(settings.COINBASE_API_KEY)

@login_required
def wallet(request):
    res = None
    if request.method == "POST" and not request.user.pay_id:
        res = coinbase.create_charge(name="Order", description="Payment", pricing_type="no_price")
        request.user.pay_id = res["data"]["code"]
        User.objects.filter(id=request.user.id).update(pay_id=res["data"]["code"])
        tx = Transaction.objects.create(pay_id=res["data"]["code"], user=request.user)

    if request.user.pay_id:
        res = coinbase.get_charge(request.user.pay_id)
        tx = Transaction.objects.get(pay_id=res["data"]["code"])

    if res:
        addresses = res["data"]["addresses"]
        expiry_raw = res["data"]["expires_at"].replace("Z", "")
        expiry = datetime.fromisoformat(expiry_raw).strftime("%B %d, %I:%M %p")
    
    context = {"addresses": addresses.items(), "expiry": expiry, "tx": tx} if res else {}
    context.update({"txs": request.user.transactions.order_by("-date_created")[:10]})
    return render(request, 'transactions/add-money.html', context)

@login_required
def verify_tx(request, pay_id):
    tx = get_object_or_404(Transaction, pay_id=pay_id, user=request.user)
    if tx.status == TransactionStatus.CONFIRMED:
        messages.success(request, "Transaction already completed")
        return redirect("transactions")
    elif tx.status == TransactionStatus.EXPIRED:
        messages.error(request, "Transaction Expired")
        return redirect("transactions")
    try:
        res = coinbase.get_charge(pay_id)
        status = confirm_payment(res)
        tx.status = status
        if status == TransactionStatus.PENDING:
            messages.error(request, "Transaction Pending")
        elif status == TransactionStatus.CONFIRMED:
            amt = float(res["data"]["payments"][0]["value"]["local"]["amount"])
            tx.amount = amt
            user = User.objects.filter(id=request.user.id)
            user.update(pay_id=None, balance=user.first().balance+amt)
            messages.success(request, "Transaction Verified!")
        elif status == TransactionStatus.EXPIRED:
            User.objects.filter(id=request.user.id).update(pay_id=None)
            messages.error(request, "Transaction Expired")
        tx.save()
    except:
        messages.error(request, "Something went wrong")
    return redirect("wallet")
