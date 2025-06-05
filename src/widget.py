from black import datetime
from src.masks import get_mask_account, get_mask_card_number


def get_date(date_str: str) -> str:
    """Функция переформатирования даты"""
    return datetime.fromisoformat(date_str).strftime("%d.%m.%Y")


def mask_account_card(bank_accounts: str) -> str:
    """Функция для обработки ввода банковских реквиизитов"""
    if bank_accounts == '\n':
        return "empty string"
    new_line = bank_accounts.split()
    if new_line[0] == "Счет":
        if new_line[-1].isdigit():
            masked_line = get_mask_account(new_line[-1])
            new_line[-1] = masked_line
    elif new_line[-1].isdigit() :
        masked_line = get_mask_card_number(new_line[-1])
        new_line[-1] = masked_line
    else:
        return "wrong data"

    return " ".join(new_line)


