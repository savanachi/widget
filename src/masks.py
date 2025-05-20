"""
Функция для считывания входных данных и определения что
подаётся на вход: номер карты или счёт и выбора соот-
ветствующей функции для маскирования
"""

def get_reqiusits(bank_accounts: str) -> str :
    """Функция для обработки ввода банковских реквиизитов"""
    new_line = bank_accounts.split()
    if new_line[0] == 'Счет' :
        masked_line = get_mask_account(new_line[-1])
        new_line[-1] = masked_line
    else:
        masked_line = get_mask_card_number(new_line[-1])
        new_line[-1] = masked_line

    return " ".join(new_line)



"""
Функция get_mask_card_number принимает на вход номер карты и
возвращает ее маску. Номер карты замаскирован и отображается в формате
XXXX XX** **** XXXX, где X — это цифра номера. То есть видны первые 6 цифр
и последние 4 цифры, остальные символы отображаются звездочками, номер разбит
по блокам по 4 цифры, разделенным пробелами. Пример работы функции:
7000792289606361     # входной аргумент
7000 79** **** 6361  # выход функции
"""


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и маскирует цифры номера."""

    card_list = list(card_number)
    for index in range(len(card_number)):
        if 6 <= index <= 11:
            card_list[index] = "*"

    masked_str = "".join(card_list)
    card_str = " ".join(masked_str[i : i + 4] for i in range(0, len(masked_str), 4))

    return card_str


"""
Функция get_mask_account принимает на вход номер счета и
возвращает его маску. Номер счета замаскирован и отображается в
формате **XXXX, где X — это цифра номера. То есть видны только
последние 4 цифры номера, а перед ними — две звездочки.
Пример работы функции:
73654108430135874305  # входной аргумент
**4305  # выход функции
"""


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счёта и возвращает маску."""

    masked_acc = list(account_number[-6:])
    for i in range(0, 2):
        masked_acc[i] = "*"

    masked_str = "".join(masked_acc)
    return masked_str
