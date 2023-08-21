import json
from django.core.serializers import serialize
import uuid

from django.db import models

from authentication.models import User
# Create your models here.
from utils.constants import CreditCard
from django.forms.models import model_to_dict


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class News(BaseModel):
    title = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "News"


class CCBase(BaseModel):
    name = models.CharField(max_length=255)


class CC(BaseModel):
    base = models.ForeignKey(CCBase, on_delete=models.CASCADE, null=True)
    cc = models.CharField(max_length=16)
    cc_type = models.CharField(max_length=255, choices=CreditCard.choices, default=CreditCard.choices[0][0])
    month = models.IntegerField()
    year = models.IntegerField()
    cvv = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    address = models.TextField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.CharField(max_length=10)
    country = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    ssn = models.CharField(max_length=255, null=True, blank=True)
    DOB = models.DateField(null=True, blank=True)
    price = models.FloatField()
    purchased = models.BooleanField(default=False)
    extra = models.TextField(null=True, blank=True)


class Fullz(BaseModel):
    name = models.CharField(max_length=255)
    DOB = models.DateField(null=True, blank=True)
    category = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip = models.CharField(max_length=10)
    description = models.TextField()
    price = models.FloatField()
    purchased = models.BooleanField(default=False)
    extra = models.TextField(null=True, blank=True)


class Dumps(BaseModel):
    bin = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    cc_type = models.CharField(max_length=255, choices=CreditCard.choices)
    country = models.CharField(max_length=255)
    bank = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    purchased = models.BooleanField(default=False)
    extra = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Dumps"


class Logs(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255)
    price = models.FloatField()
    purchased = models.BooleanField(default=False)
    extra = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Logs"


class Guides(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255)
    price = models.FloatField()
    purchased = models.BooleanField(default=False)
    extra = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Guides"


class Services(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255)
    price = models.FloatField()
    purchased = models.BooleanField(default=False)
    extra = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Services"


class CartProduct(BaseModel):
    product = models.CharField(max_length=64)
    product_id = models.UUIDField()
    user = models.ForeignKey(User, models.CASCADE, related_name="cart")

    def get_data(self):
        data = {"cc": CC, "dumps": Dumps, "fullz": Fullz, "logs": Logs, "guides": Guides, "services": Services}
        try:
            obj = data[self.product].objects.get(id=self.product_id)
        except:
            return None
        if obj.purchased:
            self.delete()
            return
        obj.product = self.product.upper()
        obj.cart_id = self.id
        return obj


class Order(BaseModel):
    product = models.CharField(max_length=64)
    product_id = models.UUIDField()
    user = models.ForeignKey(User, models.CASCADE, related_name="orders")

    def get_data(self):
        data = {"cc": CC, "dumps": Dumps, "fullz": Fullz, "logs": Logs, "guides": Guides, "services": Services}
        try:
            obj = data[self.product].objects.get(id=self.product_id)
        except:
            return None
        if self.product not in ["guides", "services"]:
            obj.purchased = True
        obj.save()
        data = str(serialize("json", [obj]))
        data = json.loads(data)[0]["fields"]
        data.pop("date_created")
        data.pop("purchased")
        data.pop("base", None)
        obj.data = str(data).replace("'", '').replace(", ", "\n").replace("{", "").replace("}", "")
        obj.product = self.product.upper()
        obj.date_created = self.date_created
        return obj
