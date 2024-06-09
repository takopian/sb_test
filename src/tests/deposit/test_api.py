from datetime import datetime

from aiohttp.test_utils import AioHTTPTestCase

from app import create_app
from deposit.utils import DATE_FORMAT, calculate_deposit_balance


class TestDepositView(AioHTTPTestCase):
    async def get_application(self):
        app = create_app(None)
        return app

    async def test_get_deposit_balance(self):
        params = {
            "date": "01.01.2022",
            "periods": 12,
            "amount": 10000,
            "rate": 5.0
        }

        request = await self.client.request("GET", "/deposit", params=params)
        assert request.status == 200
        response = await request.json()
        application_date = datetime.strptime(
            params.pop("date"), DATE_FORMAT
        ).date()
        expected_response = {
            date.strftime(DATE_FORMAT): str(val)
            for date, val in calculate_deposit_balance(
                application_date, **params
            )
        }
        self.assertEqual(response, expected_response)

    async def test_get_deposit_balance_bad_request(self):
        params = {
            "date": "2022-01-01",
            "amount": 10000,
            "rate": 10
        }

        request = await self.client.request("GET", "/deposit", params=params)

        assert request.status == 400
        response = await request.json()
        self.assertEqual(
            response["error"],
            {
                'date': ['Not a valid date.'],
                'periods': ['Missing data for required field.'],
                'rate': ['Invalid value.']
            }
        )
