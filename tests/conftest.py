import pytest


@pytest.fixture
def transactions():
    return [
        {"id": 41428829, "state": "EXECUTED",
         "date": "2019-07-03T18:35:29.512"},
        {"id": 939719570, "state": "EXECUTED",
         "date": "2018-06-30T02:08:58.425"},
        {"id": 594226727, "state": "CANCELED",
         "date": "2018-09-12T21:27:25.241"},
        {"id": 615064591, "state": "CANCELED",
         "date": "2018-10-14T08:21:33.419"},
    ]


@pytest.fixture
def transactions_missing_keys():
    return [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2},
        {},
    ]


@pytest.fixture
def transactions_equal_dates():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-01-01T00:00:00.000"},
        {"id": 2, "state": "CANCELED", "date": "2024-01-01T00:00:00.000"},
        {"id": 3, "state": "EXECUTED", "date": "2024-01-01T00:00:00.000"},
    ]


@pytest.fixture
def transactions_wrong_date_format():
    return [
        {"id": 1, "date": "01-01-2024"},
        {"id": 2, "date": "2024-01-01T00:00:00.000"},
    ]


# Фикстура для generators — тоже сюда
@pytest.fixture
def transactions_with_currency():
    return [
        {
            "id": 1,
            "description": "Перевод организации",
            "operationAmount": {"currency": {"code": "USD"}},
        },
        {
            "id": 2,
            "description": "Перевод со счета на счет",
            "operationAmount": {"currency": {"code": "RUB"}},
        },
        {
            "id": 3,
            "description": "Перевод с карты на карту",
            "operationAmount": {"currency": {"code": "USD"}},
        },
    ]
