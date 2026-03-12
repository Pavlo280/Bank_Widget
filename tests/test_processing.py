"""
Тесты для модуля processing.
"""

from src.processing import filter_by_state, sort_by_date


TRANSACTIONS = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419"},
]


def test_filter_by_state_default():
    result = filter_by_state(TRANSACTIONS)
    assert len(result) == 2
    assert all(t["state"] == "EXECUTED" for t in result)


def test_filter_by_state_canceled():
    result = filter_by_state(TRANSACTIONS, "CANCELED")
    assert len(result) == 2
    assert all(t["state"] == "CANCELED" for t in result)


def test_filter_by_state_empty():
    result = filter_by_state(TRANSACTIONS, "PENDING")
    assert result == []


def test_sort_by_date_descending():
    result = sort_by_date(TRANSACTIONS)
    dates = [t["date"] for t in result]
    assert dates == sorted(dates, reverse=True)


def test_sort_by_date_ascending():
    result = sort_by_date(TRANSACTIONS, reverse=False)
    dates = [t["date"] for t in result]
    assert dates == sorted(dates)
