import json
from typing import Any


def get_transactions(file_path: str) -> list[dict[str, Any]]:
    """Читает JSON-файл по пути file_path и возвращает список транзакций.

    Если файл не найден, содержит невалидный JSON или корень не является
    списком — возвращает пустой список.
    """
    try:
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    if not isinstance(data, list):
        return []
    return data
