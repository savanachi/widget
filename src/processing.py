def filter_by_state(my_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция принимает на вход список словарей и возвращает
         только указанные в ключе state"""
    return [my_list for my_list in my_list if my_list.get("state") == state]


def sort_by_date(my_list: list[dict], direction: bool = 1) -> list[dict]:
    """Функция сортировки по дате"""

    return new_list


