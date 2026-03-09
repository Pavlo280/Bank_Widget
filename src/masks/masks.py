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
    return f"{card_str[:4]} {card_str[4:6]}** **** {card_str[12:]}"


def get_mask_account(account_number: int) -> str:
    """Маскирует номер банковского счёта.

    Принимает номер счёта в виде числа и возвращает строку
    с маской по правилу: **XXXX (последние 4 цифры).

    Args:
        account_number: Номер банковского счёта.

    Returns:
        Строка с замаскированным номером счёта.
    """
    account_str = str(account_number)
    return f"**{account_str[-4:]}"
