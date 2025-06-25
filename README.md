### Домашнее Задание 11.2

### Написание тестов для проекта виджетов для банковских карт.
 Пишем тесты для файлов masks.py, processing.py, widget.py
соответственно test_masks.py, test_porcessing.py, test_widget.py

Дописал модуль decorators.py & tests_decorators.py в основной 
проект. В модуле tests_decorators.py написали тестовые функции
для проверки модуля decorators.py

Тесты запускаются командой: pytest -v . 
Для вывода на экран процента покрытия нужно запустить
команду: pytest -v --cov=src.
Для создания HTML-ОТЧЁТА запускается следующая комада:
pytest --cov=src --cov-report=html.


### Список зависимостей:
* from typing import Any, Dict, List
* from 'src.widget' import get_requisites, get_date
* from 'src.processing' import filter_by_state, sort_by_date
* from black import datetime

Основными рабочими файлами являются файлы widget.py и 
processing.py. Файл main.py является файлом запуска.

