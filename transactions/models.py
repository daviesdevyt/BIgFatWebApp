from django.db import models
from base.models import BaseModel
from utils.constants import TransactionStatus
# Create your models here.

class Transaction(BaseModel):
    amount = models.FloatField(null=True, blank=True)
    pay_id = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=TransactionStatus.choices, default=TransactionStatus.PENDING)
    user = models.ForeignKey("authentication.User", on_delete=models.CASCADE, related_name="transactions")
