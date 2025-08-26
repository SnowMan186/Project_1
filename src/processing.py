from typing import List, Dict
from datetime import datetime


def filter_by_state(transactions: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """ Фильтрация списка операций по указанному статусу. """
    return [t for t in transactions if t.get('state') == state]


def sort_by_date(transactions: List[Dict], ascending: bool = False) -> List[Dict]:
    """ Сортировка операций по дате выполнения. """
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
print(filtered_transactions)

sorted_transactions = sort_by_date(transactions)
print(sorted_transactions)