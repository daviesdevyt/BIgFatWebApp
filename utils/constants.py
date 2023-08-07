class CreditCard:
    choices = (
        ("Visa", "Visa"), ("Mastercard", "Mastercard"), ("Amex", "Amex"), ("Discover", "Discover"), ("JCB", "JCB"),
        ("Diners Club", "Diners Club"))

class TransactionStatus:
    PENDING = "PENDING"
    CANCELLED= "CANCELLED"
    CONFIRMED = "CONFIRMED"
    EXPIRED = "EXPIRED"
    choices = (
        (PENDING, "PENDING"), (CANCELLED, "CANCELLED"), (CONFIRMED, "CONFIRMED")
    )