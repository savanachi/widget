from typing import Any, Dict, List


def filter_by_state(my_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция принимает на вход список словарей и возвращает
    только указанные в ключе state"""
    return [my_list for my_list in my_list if my_list.get("state") == state]


def sort_by_date(operation_list: List[Dict[str, Any]], direction: bool = True) -> list[Dict[str, Any]]:
    """Функция сортировки по дате"""

    return sorted(operation_list, key=lambda item: item["date"], reverse=direction)
