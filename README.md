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
```

## Модуль utils — чтение JSON

```python
from src.utils import get_transactions

transactions = get_transactions("data/operations.json")
```

Возвращает список транзакций. При отсутствии файла, невалидном JSON или
если корень не является списком — возвращает `[]`.

## Модуль external_api — конвертация валют

Конвертирует сумму транзакции в рубли. Для USD/EUR обращается к
Exchange Rates Data API (apilayer). Для RUB возвращает сумму без запроса.

```python
from src.external_api import convert_to_rub

amount_rub = convert_to_rub(transaction)
```

Требует переменную окружения `EXCHANGE_RATES_API_KEY`. Скопируйте
`.env.example` в `.env` и вставьте свой ключ:

```bash
cp .env.example .env
# затем откройте .env и заполните EXCHANGE_RATES_API_KEY=ваш_ключ
```
