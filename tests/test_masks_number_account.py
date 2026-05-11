import pytest
from src.masks import get_mask_card_number, get_mask_account

# def test_get_mask_card_number():
#     number = '1246953785126548'
#     expected = '1246 95** **** 6548'
#     result = get_mask_card_number(number)
#     assert result == expected
#
#
# def test_get_mask_card_number_2():
#     number = '246537851246548'
#     expected = '2465 37**** *6548'
#     result = get_mask_card_number(number)
#     assert result == expected
#
#
# def test_get_mask_card_number_3():
#     number = '1246953785126548123'
#     expected = '1246 95** **** **** 123'
#     result = get_mask_card_number(number)
#     assert result == expected
#
# def test_get_mask_card_number_4():
#     number = 'Bunkkardnumber'
#     expected = 'Карта введена не правильно'
#     result = get_mask_card_number(number)
#     assert result == expected


@pytest.mark.parametrize("number, expected", [
    ("1246953785126548", "1246 95** **** 6548"),
    ("246537851246548", "2465 37**** *6548"),
    ("1246953785126548123", "1246 95** **** **** 123"),
    ("Bunkkardnumber", "Ошибка"),
    ("", "Ошибка"),
])
def test_masks_number(number, expected):
    assert get_mask_card_number(number) == expected


@pytest.mark.parametrize("account_input, expected_result", [
    ("73654108430135874305", "**4305"),
    ("GB1234567890", "**7890"),
    ("RU 7365 4108 4301 3587 4305", "**4305"),
    ("1234", "Ошибка"),
    ("123", "Ошибка"),
    ("", "Ошибка")
])
def test_get_mask_account_logic(account_input, expected_result):
    result = get_mask_account(account_input)
