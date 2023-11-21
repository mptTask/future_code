import requests

class CurrencyConverter:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://v6.exchangerate-api.com/v6/{}".format(api_key)

    def get_exchange_rate(self, base_currency, target_currency):
        url = "{}/pair/{}/{}".format(self.base_url, base_currency, target_currency)
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data['result'] == 'success':
                exchange_rate = data['conversion_rate']
                return exchange_rate
            else:
                print("Не удалось получить курсы валют. Пожалуйста, проверьте коды валют и повторите попытку.")
                return None
        else:
            print("Не удалось получить курсы валют. Пожалуйста, проверьте свой API-ключ и повторите попытку.")
            return None

    def convert_currency(self, amount, base_currency, target_currency):
        exchange_rate = self.get_exchange_rate(base_currency, target_currency)
        if exchange_rate is not None:
            converted_amount = amount * exchange_rate
            return converted_amount
        else:
            return None

api_key = '3b2360c9437e7469c094c333'
converter = CurrencyConverter(api_key)

base_currency = input("Введите код базовой валюты (например, USD): ")
target_currency = input("Введите код целевой валюты (например, EUR): ")
amount = float(input("Введите количество валюты для конвертации: "))

exchange_rate = converter.get_exchange_rate(base_currency, target_currency)
if exchange_rate is not None:
    converted_amount = converter.convert_currency(amount, base_currency, target_currency)
    print("{:.2f} {} равны {:.2f} {}".format(amount, base_currency, converted_amount, target_currency))
else:
    print("Конвертация не выполнена.")
