import pytest

from src.widget import get_date
from src.widget import mask_account_card


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("счет 12345678901234567890", "Счет **7890"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("MasterCard 7158300714726758", "MasterCard 7158 30** **** 6758"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Visa Platinum 1234567812345678", "Visa Platinum 1234 56** **** 5678"),
    ],
)
def test_mask_account_card_valid(input_data, expected_output) -> None:
    assert mask_account_card(input_data) == expected_output


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ("", "Ошибка"),
        ("VisaClassic", "Ошибка"),
        ("Visa 123", "Ошибка"),
        ("Visa Classic ABCD", "Ошибка"),
        ("Visa ASDRTIPKJHYGVNFD", "Ошибка"),
        ("Счет DGHJTRUOPLJHKLLJH", "Ошибка"),
        ("Счет 123", "Ошибка"),
        ("1234567812345678", "Ошибка"),
    ],
)
def test_mask_account_card_invalid(input_data, expected_output) -> None:
    assert mask_account_card(input_data) == expected_output


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2000-01-01T00:00:00.000000", "01.01.2000"),
        ("1999-12-31T23:59:59.999999", "31.12.1999"),
        ("2024-01-01T00:00:00.000000", "01.01.2024"),
        ("2024-12-31T23:59:59.999999", "31.12.2024"),
    ],
)
def test_get_date_valid(input_data, expected_output) -> None:
    assert get_date(input_data) == expected_output


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ("", "Ошибка"),
        ("T02:26:18.671407", "Ошибка"),
        ("просто строка", "Ошибка"),
        ("2024", "Ошибка"),
    ],
)
def test_get_date_invalid(input_data, expected_output) -> None:
    assert get_date(input_data) == expected_output
