import pytest

import src.masks.generators


# фикстура transactions_with_currency берётся из conftest.py


def test_filter_by_currency_usd(transactions_with_currency):
    result = list(
        src.masks.generators.filter_by_currency(transactions_with_currency,
                                                "USD")
    )
    assert len(result) == 2


def test_filter_by_currency_rub(transactions_with_currency):
    result = list(
        src.masks.generators.filter_by_currency(transactions_with_currency,
                                                "RUB")
    )
    assert len(result) == 1


def test_filter_by_currency_no_match(transactions_with_currency):
    result = list(
        src.masks.generators.filter_by_currency(transactions_with_currency,
                                                "EUR")
    )
    assert result == []


def test_filter_by_currency_empty():
    result = list(src.masks.generators.filter_by_currency([],
                                                          "USD"))
    assert result == []


def test_transaction_descriptions(transactions_with_currency):
    descriptions = src.masks.generators.transaction_descriptions(
        transactions_with_currency
    )
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"


def test_transaction_descriptions_empty():
    result = list(src.masks.generators.transaction_descriptions([]))
    assert result == []


def test_card_number_generator_format():
    result = list(src.masks.generators.card_number_generator(1, 1))
    assert result[0] == "0000 0000 0000 0001"


def test_card_number_generator_range():
    result = list(src.masks.generators.card_number_generator(1, 5))
    assert len(result) == 5


@pytest.mark.parametrize(
    "start, stop, expected_count",
    [
        (1, 5, 5),
        (1, 1, 1),
        (10, 15, 6),
    ],
)
def test_card_number_generator_parametrized(start, stop, expected_count):
    result = list(src.masks.generators.card_number_generator(start, stop))
    assert len(result) == expected_count
