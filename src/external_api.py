import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()


def convert_to_rub(transaction: dict[str, Any]) -> float:
    """Возвращает сумму транзакции в рублях.

    Если валюта уже RUB — возвращает amount как float без обращения к API.
    Для USD и EUR запрашивает текущий курс через Exchange Rates Data API
    (apilayer) и конвертирует сумму. Ключ API читается из переменной
    окружения EXCHANGE_RATES_API_KEY.
    """
    operation = transaction["operationAmount"]
    amount = float(operation["amount"])
    currency_code: str = operation["currency"]["code"]

    if currency_code == "RUB":
        return amount

    api_key = os.getenv("EXCHANGE_RATES_API_KEY", "")
    url = "https://api.apilayer.com/exchangerates_data/latest"
    response = requests.get(
        url,
        headers={"apikey": api_key},
        params={"base": currency_code, "symbols": "RUB"},
    )
    response.raise_for_status()
    rate: float = response.json()["rates"]["RUB"]
    return amount * rate
