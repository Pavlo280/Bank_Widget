"""
Модуль содержит функции для работы с банковскими картами и счетами.
"""

from src.masks.masks import get_mask_account
from src.masks.masks import get_mask_card_number


def mask_account_card(card_or_account: str) -> str:
    """
    Маскирует номер карты или счета в зависимости от типа.
    """
    if not card_or_account:
        return "Ошибка"
    # Разделяем строку на части
    parts = card_or_account.split()

    if len(parts) < 2:
        return "Ошибка"

    try:
        if parts[0].lower() == "счет":
            account_number = int(parts[-1])
            masked_number = get_mask_account(account_number)
            if masked_number == "Ошибка":
                return "Ошибка"
            return f"Счет {masked_number}"
        else:
            card_name = " ".join(parts[:-1])
            card_number = int(parts[-1])
            masked_number = get_mask_card_number(card_number)
            if masked_number == "Ошибка":
                return "Ошибка"
            return f"{card_name} {masked_number}"

    except ValueError:
        return "Ошибка"


def get_date(date_string: str) -> str:
    """
    Преобразует дату из формата "2024-03-11T02:26:18.671407" в "ДД.ММ.ГГГГ".
    """
    if not date_string:
        return "Ошибка"
    try:
        date_part = date_string.split("T")[0]
        if not date_part:
            return "Ошибка"
        parts = date_part.split("-")
        if len(parts) != 3:
            return "Ошибка"
        year, month, day = parts
        if not (year.isdigit() and month.isdigit() and day.isdigit()):
            return "Ошибка"
        return f"{day}.{month}.{year}"
    except Exception:
        return "Ошибка"
