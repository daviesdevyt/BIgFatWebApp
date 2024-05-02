import requests


class GenericSerializer:
    def __init__(self, data) -> None:
        for var, value in data.items():
            if isinstance(value, dict):
                setattr(self, var, GenericSerializer(value))
                continue
            setattr(self, var, value)

    def __getattr__(self, __name: str):
        return None


class Plisio:
    def __init__(self, plisio_key) -> None:
        self.plisio_key = plisio_key


    def create_invoice(self, amount, currency, order_number, order_name):
        response = requests.get(
            f"https://api.plisio.net/api/v1/invoices/new?source_amount={amount}&source_currency=USD&order_number={order_number}&currency={currency.upper()}&order_name={order_name}&api_key={self.plisio_key}",
        )
        if response.status_code == 200:
            return GenericSerializer(response.json()["data"])
        raise Exception("Failed to create invoice: " + str(response.status_code))

    def get_operation(self, tx_id):
        response = requests.get(
            f"https://api.plisio.net/api/v1/operations/{tx_id}?api_key={self.plisio_key}",
        )
        if response.status_code == 200:
            return GenericSerializer(response.json()["data"])
        raise Exception("Failed to retrieve invoice: " + str(response.status_code))
