class CreditCard:
    choices = (
        ("Visa", "Visa"), ("Mastercard", "Mastercard"), ("Amex", "Amex"), ("Discover", "Discover"), ("JCB", "JCB"),
        ("Diners Club", "Diners Club"))

class TransactionStatus:
    # pending, completed, error, new, expired, mismatch, cancelled
    PENDING = "pending"
    COMPLETED = "completed"
    ERROR = "error"
    NEW = "new"
    EXPIRED = "expired"
    MISMATCH = "mismatch"
    CANCELLED = "cancelled"
    choices = (
        (PENDING, "pending"), (COMPLETED, "completed"), (ERROR, "error"), (NEW, "new"),
        (EXPIRED, "expired"), (MISMATCH, "mismatch"), (CANCELLED, "cancelled")
    )
    # PENDING = "PENDING"
    # CANCELLED= "CANCELLED"
    # CONFIRMED = "CONFIRMED"
    # EXPIRED = "EXPIRED"
    # choices = (
    #     (PENDING, "PENDING"), (CANCELLED, "CANCELLED"), (CONFIRMED, "CONFIRMED")
    # )