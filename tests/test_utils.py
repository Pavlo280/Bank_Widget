import json
from unittest.mock import mock_open
from unittest.mock import patch

from src.utils import get_transactions


def test_get_transactions_valid_list() -> None:
    data = [{"id": 1, "state": "EXECUTED"}, {"id": 2, "state": "CANCELED"}]
    m = mock_open(read_data=json.dumps(data))
    with patch("builtins.open", m):
        result = get_transactions("any_path.json")
    assert result == data


def test_get_transactions_empty_file() -> None:
    m = mock_open(read_data="")
    with patch("builtins.open", m):
        result = get_transactions("any_path.json")
    assert result == []


def test_get_transactions_not_a_list() -> None:
    m = mock_open(read_data=json.dumps({"key": "value"}))
    with patch("builtins.open", m):
        result = get_transactions("any_path.json")
    assert result == []


def test_get_transactions_file_not_found() -> None:
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = get_transactions("missing.json")
    assert result == []


def test_get_transactions_invalid_json() -> None:
    m = mock_open(read_data="{ not valid json [[[")
    with patch("builtins.open", m):
        result = get_transactions("any_path.json")
    assert result == []
