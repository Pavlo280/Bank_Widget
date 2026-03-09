"""
Модуль содержит функции для работы с банковскими картами и счетами.
"""

from src.masks.masks import get_mask_account
from src.masks.masks import get_mask_card_number


def mask_account_card(card_or_account: str) -> str:
    """
    Маскирует номер карты или счета в зависимости от типа.
    """
    # Разделяем строку на части
    parts = card_or_account.split()

    # Определяем тип (карта или счет)
    if parts[0].lower() == "счет":
        # Для счета - маскируем последние цифры
        account_number = int(parts[-1])
        masked_number = get_mask_account(account_number)
        return f"Счет {masked_number}"
    else:
        card_name = " ".join(parts[:-1])
        card_number = int(parts[-1])
        masked_number = get_mask_card_number(card_number)
        return f"{card_name} {masked_number}"


def get_date(date_string: str) -> str:
    """
    Преобразует дату из формата "2024-03-11T02:26:18.671407" в "ДД.ММ.ГГГГ".
    """
    # Извлекаем только дату из строки
    date_part = date_string.split('T')[0]
    # Разбиваем на компоненты
    year, month, day = date_part.split('-')
    # Возвращаем в нужном формате
    return f"{day}.{month}.{year}"
