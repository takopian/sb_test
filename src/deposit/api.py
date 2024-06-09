from aiohttp import web
from aiohttp_apispec import docs, querystring_schema

from deposit.spec import DepositRequestSchema, DepositResponseSchema
from deposit.utils import DATE_FORMAT, calculate_deposit_balance


class DepositView(web.View):

    @docs(
        tags=['deposit'],
        summary='Get the deposit balance.',
        description='Get the deposit balance for every month of '
                    'the deposit period.',
        responses={
            200: {
                'description': 'A dictionary mapping date '
                               'strings to float values.',
                'schema': DepositResponseSchema
            },
            400: {'description': 'Invalid input data'},
        }
    )
    @querystring_schema(DepositRequestSchema(), put_into="validated_data")
    async def get(self):
        data = self.request["validated_data"]
        balance = calculate_deposit_balance(
                data["date"], data["periods"], data["amount"], data["rate"]
            )
        return web.json_response(
            {date.strftime(DATE_FORMAT): str(val) for date, val in balance}
        )
