import pytest

from src.processing import filter_by_state
from src.processing import sort_by_date


@pytest.mark.parametrize(
    "state, expected_count",
    [
        ("EXECUTED", 2),
        ("CANCELED", 2),
        ("PENDING", 0),
        ("UNKNOWN", 0),
    ],
)
def test_filter_by_state_parametrized(transactions, state, expected_count):
    result = filter_by_state(transactions, state)
    assert len(result) == expected_count
    assert all(t["state"] == state for t in result)


def test_filter_by_state_default(transactions):
    result = filter_by_state(transactions)
    assert len(result) == 2
    assert all(t["state"] == "EXECUTED" for t in result)


def test_filter_by_state_empty_list():
    assert filter_by_state([]) == []


def test_filter_by_state_missing_key(transactions_missing_keys):
    result = filter_by_state(transactions_missing_keys, "EXECUTED")
    assert len(result) == 1


def test_filter_by_state_returns_new_list(transactions):
    result = filter_by_state(transactions, "EXECUTED")
    assert result is not transactions


def test_filter_by_state_none_value():
    data = [{"id": 1, "state": None}]
    assert filter_by_state(data, "EXECUTED") == []


def test_filter_by_state_case_sensitive():
    data = [{"id": 1, "state": "executed"}]
    assert filter_by_state(data, "EXECUTED") == []


def test_sort_by_date_descending(transactions):
    result = sort_by_date(transactions)
    dates = [t["date"] for t in result]
    assert dates == sorted(dates, reverse=True)


def test_sort_by_date_ascending(transactions):
    result = sort_by_date(transactions, reverse=False)
    dates = [t["date"] for t in result]
    assert dates == sorted(dates)


def test_sort_by_date_empty_list():
    assert sort_by_date([]) == []


def test_sort_by_date_single_item():
    data = [{"id": 1, "date": "2024-01-01T00:00:00.000"}]
    assert sort_by_date(data) == data


def test_sort_by_date_equal_dates(transactions_equal_dates):
    result = sort_by_date(transactions_equal_dates)
    dates = [t["date"] for t in result]
    assert dates[0] == dates[1] == dates[2]


def test_sort_by_date_wrong_format(transactions_wrong_date_format):
    result = sort_by_date(transactions_wrong_date_format, reverse=False)
    assert result[0]["id"] == 1


def test_sort_by_date_missing_key(transactions_missing_keys):
    with pytest.raises(KeyError):
        sort_by_date(transactions_missing_keys)
