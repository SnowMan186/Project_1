from typing import List, Dict
from datetime import datetime


def filter_by_state(transactions: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """Фильтрует транзакции по заданному состоянию. Args: transactions (List[Dict]): Список словарей с операциями. state (str): Статус операций ('EXECUTED' по умолчанию). Returns: List[Dict]: Отфильтрованный список операций. """
    return [t for t in transactions if t.get('state') == state]


def sort_by_date(transactions: List[Dict], ascending: bool = False) -> List[Dict]:
    """Сортирует операции по дате. Args: transactions (List[Dict]): Список словарей с операциями. ascending (bool): Если True, сортировка по возрастанию дат (по умолчанию False). Returns: List[Dict]: Отсортированный список операций. """
    sorted_transactions = sorted(
        transactions,
        key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'),
        reverse=not ascending
    )
    return sorted_transactions


transactions = [
    {'id': 1, 'state': 'EXECUTED', 'date': '2023-07-01'},
    {'id': 2, 'state': 'CANCELED', 'date': '2023-07-02'},
    {'id': 3, 'state': 'EXECUTED', 'date': '2023-07-03'}
]

filtered_transactions = filter_by_state(transactions)
print(filtered_transactions)  # Результат: [{...}, {...}] # Только выполненные транзакции

sorted_transactions = sort_by_date(transactions)
print(sorted_transactions)     # Результат: сортируется по датам, начиная с последней