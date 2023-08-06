from django.db import models
from base.models import BaseModel
from utils.constants import TransactionStatus
# Create your models here.

class Transaction(BaseModel):
    amount = models.FloatField()
    track_id = models.IntegerField()
    status = models.CharField(max_length=255, choices=TransactionStatus.choices, default=TransactionStatus.pending)
    user = models.ForeignKey("authentication.User", on_delete=models.CASCADE, related_name="transactions")
