from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from authentication.models import User
from utils.constants import TransactionStatus
from utils.plisio_api import Plisio
from utils.helpers import random_string
from .models import Transaction
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.contrib import messages


# Create your views here.
plisio = Plisio(settings.PLISIO_API_KEY)

@login_required
def wallet(request):
    context = {}
    res = None
    if request.method == "POST" and not request.user.pay_id:
        currency = request.POST.get("currency")
        amount = request.POST.get("amount")
        res = plisio.create_invoice(amount, currency, random_string(), "Topup order")
        request.user.pay_id = res.txn_id
        request.user.save()
        Transaction.objects.create(pay_id=res.txn_id, user=request.user)

    if request.user.pay_id and not res:
        res = plisio.get_operation(request.user.pay_id)
        
    if res:
        context["invoice_url"] = res.invoice_url

    context.update({"txs": request.user.transactions.order_by("-date_created")[:10]})
    return render(request, 'transactions/add-money.html', context=context)

@login_required
def verify_tx(request, pay_id):
    tx = get_object_or_404(Transaction, pay_id=pay_id, user=request.user)
    if tx.status == TransactionStatus.COMPLETED:
        messages.success(request, "Transaction already completed")
        return redirect("transactions")
    elif tx.status == TransactionStatus.EXPIRED:
        messages.error(request, "Transaction Expired")
        return redirect("transactions")
    try:
        res = plisio.get_operation(pay_id)
        tx.status = res.status
        if res.status in [TransactionStatus.EXPIRED, TransactionStatus.CANCELLED, TransactionStatus.ERROR]:
            User.objects.filter(id=request.user.id).update(pay_id=None)
            messages.error(request, f"Transaction {res.status}")
        
        elif res.status != TransactionStatus.COMPLETED:
            messages.error(request, f"Transaction status: {res.status.title()}")

        elif res.status == TransactionStatus.COMPLETED:
            amt = float(res.source_rate*res.amount)
            tx.amount = amt
            user = User.objects.filter(id=request.user.id)
            user.update(pay_id=None, balance=user.first().balance+amt)
            messages.success(request, "Transaction Verified!")

        tx.save()
    except:
        messages.error(request, "Something went wrong")
    return redirect("wallet")
