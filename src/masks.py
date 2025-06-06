def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и маскирует цифры номера."""
    if len(card_number) > 16 or len(card_number) < 16:
        return  'wrong datas'
    card_list = list(card_number)
    for index in range(len(card_number)):
        if 6 <= index <= 11:
            card_list[index] = "*"
    masked_str = "".join(card_list)
    card_str = " ".join(masked_str[i : i + 4] for i in range(0, len(masked_str), 4))
    return card_str


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счёта и возвращает маску."""
    if len(account_number) > 20 or len(account_number) < 20:
        return 'wrong datas'
    masked_acc = list(account_number[-6:])
    for i in range(0, 2):
        masked_acc[i] = "*"
    masked_str = "".join(masked_acc)
    return masked_str
