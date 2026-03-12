"""
Модуль содержит функции для обработки списка банковских операций.
"""

from typing import List


def filter_by_state(
    transactions: List[dict], state: str = "EXECUTED"
) -> List[dict]:
    """
    Фильтрует список словарей по значению ключа state.

    Args:
        transactions: Список словарей с данными о банковских операциях.
        state: Статус операции для фильтрации. По умолчанию 'EXECUTED'.

    Returns:
        Новый список словарей с указанным статусом.
    """
    return [t for t in transactions if t.get("state") == state]


def sort_by_date(
    transactions: List[dict], reverse: bool = True
) -> List[dict]:
    """
    Сортирует список словарей по дате.

    Args:
        transactions: Список словарей с данными о банковских операциях.
        reverse: Порядок сортировки. По умолчанию True (убывание).

    Returns:
        Новый список словарей, отсортированный по дате.
    """
    return sorted(transactions, key=lambda t: t["date"], reverse=reverse)
