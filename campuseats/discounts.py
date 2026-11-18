"""Discount rules for different customer types."""


def apply_discount(total: float, rate: float, max_saving: float | None = None) -> float:
    """Return a total after applying a rate, optionally capped at a maximum saving."""
    saving = total * rate
    if max_saving is not None:
        saving = min(saving, max_saving)
    return round(total - saving, 2)


def student_discount(total: float) -> float:
    """Return the total after the 20% student discount, capped at £5."""
    return apply_discount(total, rate=0.20, max_saving=5)


def staff_discount(total: float) -> float:
    """Return the total after the 15% staff discount."""
    return apply_discount(total, rate=0.15)


def bulk_discount(total: float) -> float:
    """Return the total after the 10% bulk discount."""
    return apply_discount(total, rate=0.10)


def senior_discount(total: float) -> float:
    """Return the total after the 25% senior discount."""
    return apply_discount(total, rate=0.25)


def discount_label(pct: float) -> str:
    return f"{int(pct * 100)}% off"