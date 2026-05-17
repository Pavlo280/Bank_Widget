def filter_by_currency(transactions, currency):
    """
    Фильтрует транзакции по валюте.

    Args:
        transactions: список словарей с транзакциями
        currency: код валюты например "USD", "RUB"

    Returns:
        Итератор транзакций с указанной валютой
    """
    for transaction in transactions:
        # Достаём вложенные словари через .get()
        # чтобы не упасть если ключа нет
        operation = transaction.get("operationAmount", {})
        curr = operation.get("currency", {})
        code = curr.get("code", "")

        if code == currency:
            yield transaction


def transaction_descriptions(transactions):
    """
    Возвращает описание каждой транзакции по очереди.

    Args:
        transactions: список словарей с транзакциями

    Returns:
        Итератор строк с описаниями
    """
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start, stop):
    """
    Генерирует номера карт в формате XXXX XXXX XXXX XXXX.

    Args:
        start: начальное значение диапазона
        end: конечное значение диапазона

    Returns:
        Итератор строк с номерами карт
    """
    for number in range(start, stop + 1):
        # zfill(16) добавляет нули слева до 16 символов
        # например 1 → "0000000000000001"
        card = str(number).zfill(16)

        # Разбиваем на группы по 4
        formatted = f"{card[0:4]} {card[4:8]} {card[8:12]} {card[12:16]}"
        yield formatted
