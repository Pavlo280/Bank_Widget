from src.masks import get_mask_card_number, get_mask_account


def main() -> None:
    """Основная функция запуска программы."""
    card = 7000792289606361
    account = 73654108430135874305

    print(get_mask_card_number(card))
    print(get_mask_account(account))


if __name__ == "__main__":
    main()