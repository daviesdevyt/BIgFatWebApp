class CreditCard:
    choices = (
        ("Visa", "Visa"), ("Mastercard", "Mastercard"), ("Amex", "Amex"), ("Discover", "Discover"), ("JCB", "JCB"),
        ("Diners Club", "Diners Club"))

class TransactionStatus:
    pending = "Pending"
    cancelled = "Cancelled"
    completed = "Completed"
    choices = (
        (pending, "Pending"), (cancelled, "Cancelled"), (completed, "Completed")
    )