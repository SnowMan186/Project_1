from collections import Counter
from typing import Dict, List
import re


def process_bank_search(data: List[Dict], search: str) -> List[Dict]:
    """
    Выполняет поиск банковских операций по указанным данным и возвращает список словарей,
    у которых в поле 'description' содержится указанный поисковый запрос.

    :param data: Список словарей с данными о банковских операциях
    :param search: Строка поиска (регулярное выражение)
    :return: Список словарей, удовлетворяющих условию поиска
    """
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    results = [
        op for op in data
        if isinstance(op.get('description'), str) and pattern.search(op['description'])
    ]
    return results


def process_bank_operations(data: List[Dict], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество операций по заданным категориям.

    :param data: Список словарей с данными о банковских операциях
    :param categories: Список категорий для учета
    :return: Словарь, где ключ — категория, значение — количество операций
    """
    counts = Counter()
    for op in data:
        category = op.get('description')  # Используем категорию description
        if category in categories:
            counts[category] += 1
    return dict(counts)

