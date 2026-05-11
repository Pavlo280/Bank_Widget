import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def transactions():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419"},
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


@pytest.mark.parametrize(
    "state, expected_count",
    [
        ("EXECUTED", 2),
        ("CANCELED", 2),
        ("PENDING", 0),
        ("UNKNOWN", 0),
    ],
)
def test_filter_by_state_parametrized(transactions, state, expected_count) -> None:
    result = filter_by_state(transactions, state)
    assert len(result) == expected_count
    assert all(t["state"] == state for t in result)


def test_filter_by_state_default(transactions) -> None:
    result = filter_by_state(transactions)
    assert len(result) == 2
    assert all(t["state"] == "EXECUTED" for t in result)


def test_filter_by_state_empty_list() -> None:
    assert filter_by_state([]) == []


def test_filter_by_state_missing_key(transactions_missing_keys) -> None:
    result = filter_by_state(transactions_missing_keys, "EXECUTED")
    assert len(result) == 1


def test_filter_by_state_returns_new_list(transactions) -> None:
    result = filter_by_state(transactions, "EXECUTED")
    assert result is not transactions


def test_filter_by_state_none_value() -> None:
    data = [{"id": 1, "state": None}]
    assert filter_by_state(data, "EXECUTED") == []


def test_filter_by_state_case_sensitive() -> None:
    data = [{"id": 1, "state": "executed"}]
    assert filter_by_state(data, "EXECUTED") == []


def test_sort_by_date_descending(transactions) -> None:
    result = sort_by_date(transactions)
    dates = [t["date"] for t in result]
    assert dates == sorted(dates, reverse=True)


def test_sort_by_date_ascending(transactions) -> None:
    result = sort_by_date(transactions, reverse=False)
    dates = [t["date"] for t in result]
    assert dates == sorted(dates)


def test_sort_by_date_empty_list() -> None:
    assert sort_by_date([]) == []


def test_sort_by_date_single_item() -> None:
    data = [{"id": 1, "date": "2024-01-01T00:00:00.000"}]
    assert sort_by_date(data) == data


def test_sort_by_date_equal_dates(transactions_equal_dates) -> None:
    result = sort_by_date(transactions_equal_dates)
    dates = [t["date"] for t in result]
    assert dates[0] == dates[1] == dates[2]


def test_sort_by_date_wrong_format(transactions_wrong_date_format) -> None:
    result = sort_by_date(transactions_wrong_date_format, reverse=False)
    assert result[0]["id"] == 1


def test_sort_by_date_missing_key(transactions_missing_keys) -> None:
    with pytest.raises(KeyError):
        sort_by_date(transactions_missing_keys)
