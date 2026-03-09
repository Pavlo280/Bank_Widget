from src.masks.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card


def main() -> None:
    """Основная функция."""
    # Тестируем mask_account_card
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Счет 73654108430135874305"))

    # Тестируем get_date
    print(get_date("2024-03-11T02:26:18.671407"))

    # Если нужны функции маскировки напрямую
    print(get_mask_card_number(7000792289606361))
    print(get_mask_account(73654108430135874305))


if __name__ == "__main__":
    main()
