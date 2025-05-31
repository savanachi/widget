from black import datetime


def get_date(date_str: str) -> str:
    """Функция переформатирования даты"""
    return datetime.fromisoformat(date_str).strftime("%d.%m.%Y")


def get_reqiusits(bank_accounts: str) -> str:
    """Функция для обработки ввода банковских реквиизитов"""
    new_line = bank_accounts.split()
    if new_line[0] == "Счет":
        masked_line = get_mask_account(new_line[-1])
        new_line[-1] = masked_line
    else:
        masked_line = get_mask_card_number(new_line[-1])
        new_line[-1] = masked_line

    return " ".join(new_line)


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и маскирует цифры номера."""
    card_list = list(card_number)
    for index in range(len(card_number)):
        if 6 <= index <= 11:
            card_list[index] = "*"

    masked_str = "".join(card_list)
    card_str = " ".join(masked_str[i : i + 4] for i in range(0, len(masked_str), 4))

    return card_str


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счёта и возвращает маску."""
    masked_acc = list(account_number[-6:])
    for i in range(0, 2):
        masked_acc[i] = "*"

    masked_str = "".join(masked_acc)

    return masked_str
