import re

from collections import Counter
from typing import Dict, List


# Разработка функции для поиска по полям


def process_bank_search(data: list[dict], search_term: str) -> list[dict]:
    """
    Простой поиск банковских операций по указанному запросу в поле 'description'.

    :param data: Список словарей с банковскими операциями
    :param search_term: Термин для поиска
    :return: Список операций, содержащих заданную строку
    """
    normalized_term = search_term.lower().strip()  # Нормализуем термин
    results = []  # Сюда будем собирать совпадающие операции

    for op in data:
        desc = op.get('description', '').lower().strip()  # Преобразуем описание к нижнему регистру
        if normalized_term in desc:
            results.append(op)

    return results

#Подсчет операций по категориям

def process_bank_operations(data: List[Dict], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество операций по заданным категориям.

    :param data: Список словарей с данными о банковских операциях
    :param categories: Список категорий для учета
    :return: Словарь, где ключ — категория, значение — количество операций
    """
    counts = Counter()
    for op in data:
        cat = op.get('description')  # Поле description хранит категорию
        if cat in categories:
            counts[cat] += 1
    return dict(counts)

# Создание основной функции

def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    while True:
        print("\nВыберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")
        choice = input("Ваш выбор: ")

        if choice not in ['1', '2', '3']:
            print("Ошибка: Выберите номер от 1 до 3.")
            continue

        break

    # Загрузка данных из выбранного формата (JSON, CSV, XLSX)
    # Примечание: Здесь предполагается наличие соответствующей функции load_data_from_file(),
    # которую нужно разработать отдельно
    file_format = {'1': 'json', '2': 'csv', '3': 'xlsx'}
    selected_format = file_format[choice]
    data = load_data_from_file(selected_format)

    # Выбор статуса операций
    valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        status_input = input(f"Введите статус ({', '.join(valid_statuses)}): ").upper()
        if status_input in valid_statuses:
            break
        else:
            print(f"Статус '{status_input}' недоступен.")