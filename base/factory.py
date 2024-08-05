import factory
from factory.django import DjangoModelFactory
from .models import CC, CCBase
from factory.fuzzy import FuzzyChoice, FuzzyInteger, FuzzyDate, FuzzyFloat
from datetime import date
from utils.constants import CreditCard


class CCBaseFactory(DjangoModelFactory):
    class Meta:
        model = CCBase
    # Add any necessary fields for CCBase here

class CCFactory(DjangoModelFactory):
    class Meta:
        model = CC

    base = factory.SubFactory(CCBaseFactory)
    cc = factory.Faker('credit_card_number')
    cc_type = FuzzyChoice(CreditCard.choices)
    month = FuzzyInteger(1, 12)
    year = FuzzyInteger(2000, 2030)
    cvv = FuzzyInteger(100, 999)
    name = factory.Faker('name')
    description = factory.Faker('text')
    address = factory.Faker('address')
    city = factory.Faker('city')
    state = factory.Faker('state')
    zip = factory.Faker('zipcode')
    country = factory.Faker('country')
    phone_number = factory.Faker('phone_number')
    email = factory.Faker('email')
    ssn = factory.Faker('ssn')
    DOB = FuzzyDate(date(1950, 1, 1))
    price = FuzzyFloat(0.0, 10000.0)
    purchased = FuzzyChoice([True, False])
    extra = factory.Faker('text')