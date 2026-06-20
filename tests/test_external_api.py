from unittest.mock import MagicMock
from unittest.mock import patch

import pytest

from src.external_api import convert_to_rub


def make_transaction(amount: str, currency_code: str) -> dict:
    """Вспомогательная функция: собирает транзакцию с нужной валютой."""
    return {
        "operationAmount": {
            "amount": amount,
            "currency": {"code": currency_code},
        }
    }


def test_convert_rub_returns_amount_without_request() -> None:
    transaction = make_transaction("1000.00", "RUB")
    with patch("src.external_api.requests.get") as mock_get:
        result = convert_to_rub(transaction)
    mock_get.assert_not_called()
    assert result == 1000.0


def test_convert_usd_to_rub() -> None:
    transaction = make_transaction("100.00", "USD")
    mock_response = MagicMock()
    mock_response.json.return_value = {"rates": {"RUB": 90.0}}
    with patch("src.external_api.requests.get", return_value=mock_response):
        result = convert_to_rub(transaction)
    assert result == pytest.approx(9000.0)


def test_convert_eur_to_rub() -> None:
    transaction = make_transaction("50.00", "EUR")
    mock_response = MagicMock()
    mock_response.json.return_value = {"rates": {"RUB": 100.0}}
    with patch("src.external_api.requests.get", return_value=mock_response):
        result = convert_to_rub(transaction)
    assert result == pytest.approx(5000.0)


def test_convert_sends_correct_params() -> None:
    transaction = make_transaction("1.00", "USD")
    mock_response = MagicMock()
    mock_response.json.return_value = {"rates": {"RUB": 90.0}}
    with patch("src.external_api.requests.get", return_value=mock_response) as mock_get:
        convert_to_rub(transaction)
    call_kwargs = mock_get.call_args.kwargs
    assert call_kwargs["params"]["base"] == "USD"
    assert call_kwargs["params"]["symbols"] == "RUB"
