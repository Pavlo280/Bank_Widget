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

## Тестирование
Проект использует pytest для тестирования. Покрытие кода проверяется с помощью pytest-cov.

### Запуск тестов:
pytest
poetry run pytest --cov

## Модуль generators

### filter_by_currency
Фильтрует транзакции по валюте.
```python
usd = filter_by_currency(transactions, "USD")
print(next(usd))

## Модуль decorators

### log

Декоратор для автоматического логирования вызовов функций.

```python
from src.decorators import log

# Вывод в консоль
@log
def add(a, b):
    return a + b

add(2, 3)
# add ok result: 5

# Запись в файл
@log(filename="app.log")
def divide(x, y):
    return x / y

divide(10, 0)
# В файл: divide error: ZeroDivisionError. Inputs: (10, 0), {}
```

**При успехе:** `<имя функции> ok result: <результат>`
**При ошибке:** `<имя функции> error: <ТипОшибки>. Inputs: <args>, <kwargs>`

Исключение после логирования **пробрасывается дальше** — декоратор не глушит ошибки.
