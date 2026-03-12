# Bank Widget

Виджет для работы с банковскими операциями клиента.

## Описание

Проект содержит функции для обработки и отображения банковских операций:
- Маскировка номеров карт и счетов
- Фильтрация операций по статусу
- Сортировка операций по дате

## Установка

```bash
pip install poetry
poetry install

## Использование

### Фильтрация по статусу
```python
from src.processing import filter_by_state

operations = [
    {"id": 1, "state": "EXECUTED", "date": "2019-07-03"},
    {"id": 2, "state": "CANCELED", "date": "2018-06-30"},
]

result = filter_by_state(operations)

from src.processing import sort_by_date

result = sort_by_date(operations)