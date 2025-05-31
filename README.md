### Домашнее Задание 10.1

### Закреление работы с GitHub и реализация функций filter_by_state и sort_by_date

Функция filter_by_state() принимает список словарей и опционально значение для ключа
state(по умолчанию'EXECUTED'). Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
state соответствует указанному значению.

Функция sort_by_date() принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание). Функция должна возвращать новый список, отсортированный по дате (
date).

### Список зависимостей:
* from typing import Any, Dict, List
* from src.widget import get_reqiusits, get_date
* from src.processing import filter_by_state, sort_by_date
* from black import datetime

Основными рабочими файлами являются файлы widget.py и 
processing.py. Файл main.py является файлом запуска.

