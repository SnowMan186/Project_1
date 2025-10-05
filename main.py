import json
import csv
import pandas as pd


def load_json(filename="transactions.json"):
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)


def load_csv(filename="transactions.csv"):
    with open(filename, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)


def load_xlsx(filename="transactions.xlsx"):
    df = pd.read_excel(filename)
    return df.to_dict('records')


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    while True:
        print("\nВыберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")

        choice = input("Ваш выбор: ").strip()

        if choice not in ['1', '2', '3']:
            print("Ошибка: выберите номер от 1 до 3.")
            continue

        break

    # Выбор формата файла и соответствующих обработчиков
    file_loaders = {
        '1': load_json,
        '2': load_csv,
        '3': load_xlsx
    }

    loader_function = file_loaders.get(choice)
    transactions = loader_function()  # Реальное чтение данных из файла

    valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]

    while True:
        status_input = input(f"\nВведите статус ({', '.join(valid_statuses)}): ").upper().strip()

        if status_input in valid_statuses:
            filtered_transactions = [
                transaction for transaction in transactions
                if transaction['status'] == status_input
            ]

            print(f"Транзакций со статусом {status_input}: {len(filtered_transactions)}")
            break
        else:
            print(f"Статус '{status_input}' недоступен.")


if __name__ == "main":
    main()
