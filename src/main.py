# Создание основной функции

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

    # Загрузка данных из выбранного формата (JSON, CSV, XLSX)
    file_formats = {
        '1': 'json',
        '2': 'csv',
        '3': 'xlsx'
    }
    selected_format = file_formats.get(choice)

    # Определяем функцию загрузки данных
    def load_data_from_file(file_format):
        # Имитация загрузки данных
        return []  # Здесь мы можем добавить реальную загрузку данных позже

    data = load_data_from_file(selected_format)

    valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]

    while True:
        status_input = input(
            f"Введите статус ({', '.join(valid_statuses)}): "
        ).upper().strip()

        if status_input in valid_statuses:
            break
        else:
            print(f"Статус '{status_input}' недоступен.")