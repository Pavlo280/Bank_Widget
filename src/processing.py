"""
Модуль содержит функции для обработки списка банковских операций.
"""

from typing import List


def filter_by_state(transactions: List[dict],
                    state: str = "EXECUTED") -> List[dict]:
    return [t for t in transactions if t.get("state") == state]


def sort_by_date(transactions: List[dict], reverse: bool = True) -> List[dict]:
    return sorted(transactions, key=lambda t: t["date"], reverse=reverse)
