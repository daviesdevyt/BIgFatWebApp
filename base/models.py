from django.db import models

# Create your models here.
class BaseModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "News"

class CC(BaseModel):
    cc = models.CharField(max_length=16)
    month = models.IntegerField()
    year = models.IntegerField()
    cvv = models.IntegerField()
    name = models.CharField(max_length=255)
    address = models.TextField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.IntegerField()
    country = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    ssn = models.CharField(max_length=255, null=True, blank=True)
    DOB = models.DateField(null=True, blank=True)
    price = models.FloatField()

class Fullz(BaseModel):
    name = models.CharField(max_length=255)
    DOB = models.DateField(null=True, blank=True)
    category = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip = models.IntegerField()
    description = models.TextField()
    price = models.FloatField()

class Dumps(BaseModel):
    bin = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    cc_type = models.CharField(max_length=255, choices=(("Visa", "Visa"), ("Mastercard", "Mastercard"), ("Amex", "Amex"), ("Discover", "Discover"), ("JCB", "JCB"), ("Diners Club", "Diners Club")))
    country = models.CharField(max_length=255)
    bank = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    class Meta:
        verbose_name_plural = "Dumps"

class Logs(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255)
    extra = models.TextField()
    price = models.FloatField()
    class Meta:
        verbose_name_plural = "Logs"

class Guides(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255)
    extra = models.TextField()
    price = models.FloatField()
    class Meta:
        verbose_name_plural = "Guides"

class Services(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255)
    extra = models.TextField()
    price = models.FloatField()
    class Meta:
        verbose_name_plural = "Services"

