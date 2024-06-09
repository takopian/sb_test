import unittest
from datetime import date
from decimal import Decimal

from deposit.utils import calculate_deposit_balance


class TestCalculateDepositBalance(unittest.TestCase):

    def test_calculate_deposit_balance_basic(self):
        application_date = date(2022, 1, 15)
        periods = 3
        amount = 100
        rate = 12.0
        expected_result = [
            (date(2022, 1, 15), Decimal('101')),
            (date(2022, 2, 15), Decimal('102.01')),
            (date(2022, 3, 15), Decimal('103.03')),
        ]

        result = calculate_deposit_balance(
            application_date, periods, amount, rate
        )
        for ind, item in enumerate(expected_result):
            self.assertEqual(result[ind], item)
