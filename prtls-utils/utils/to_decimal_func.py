from decimal import Decimal, ROUND_HALF_UP

def to_decimal(value):
    return Decimal(str(value or 0)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
