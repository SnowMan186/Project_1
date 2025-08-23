from datetime import datetime


def filter_by_state(transactions, state='EXECUTED'):
    """ Фильтрует транзакции по состоянию. :param transactions: Список словарей с операциями :param state: Статус операций ('EXECUTED' по умолчанию) :return: Отфильтрованный список операций """
    return [t for t in transactions if t.get('state') == state]


def sort_by_date(transactions, ascending=False):
    """ Сортирует операции по дате. :param transactions: Список словарей с операциями :param ascending: Если True, сортируем по возрастанию дат (по умолчанию False) :return: Отсортированный список операций """
    sorted_transactions = sorted(
        transactions,
        key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'),
        reverse=not ascending
    )
    return sorted_transactions

