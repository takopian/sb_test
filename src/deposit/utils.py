from datetime import date
from decimal import Decimal

from dateutil.relativedelta import relativedelta

DATE_FORMAT = "%d.%m.%Y"


def calculate_deposit_balance(
        application_date: date, periods: int, amount: int, rate: float
) -> list[tuple[date, Decimal]]:
    result = []
    curr_date = application_date
    curr_amount = Decimal(str(amount))
    rate = Decimal(str(rate))
    for _ in range(periods):
        curr_amount = curr_amount * (1 + rate / 12 / 100)
        result.append((curr_date, curr_amount.quantize(Decimal('0.01'))))
        curr_date = curr_date + relativedelta(months=1)
    return result
