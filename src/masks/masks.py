def get_mask_card_number(card_number: int) -> str:
    """Маскирует номер банковской карты.

    Принимает номер карты в виде числа и возвращает строку
    с маской по правилу: XXXX XX** **** XXXX.

    Args:
        card_number: Номер банковской карты (16 цифр).

    Returns:
        Строка с замаскированным номером карты.
    """
    card_str = str(card_number)
    if not card_str.isdigit():
        return "Ошибка"
    if len(card_str) == 16:
        return f"{card_str[:4]} {card_str[4:6]}** **** {card_str[12:]}"
    elif len(card_str) == 15:
        return f"{card_str[:4]} {card_str[4:6]}**** *{card_str[11:]}"
    elif len(card_str) > 16:
        return f"{card_str[:4]} {card_str[4:6]}** **** **** {card_str[-3:]}"
    else:
        return "Ошибка"


def get_mask_account(account_number: int) -> str:
    """Маскирует номер банковского счёта.

    Принимает номер счёта в виде числа и возвращает строку
    с маской по правилу: **XXXX (последние 4 цифры).
    """
    account_str = str(account_number).replace(" ", "")
    if not account_str.isdigit():
        return "Ошибка"
    if len(account_str) > 4:
        return f"**{account_str[-4:]}"
    else:
        return "Ошибка"
