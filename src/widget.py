from datetime import datetime


def mask_account_card(card_or_account_string):
    """ Функция для маскирования номеров банковских карт и счетов. :param card_or_account_string: Строка вида 'Visa Platinum 7000792289606361' или 'Счет 73654108430135874305' :return: Маскированная строка вида '**** **** **** 6361' или '** ** *** ** ********* 4305' """
    parts = card_or_account_string.split()
    if len(parts) > 1 and parts[-1].isnumeric():
        number = parts[-1]
        prefix = ' '.join(parts[:-1])

        # Если это карта, применяем стандартную маску карты
        masked_number = f"{'*' * len(number[:-4])}{number[-4:]}"

        # Если это счёт, используем специальную маску счёта
        elif len(number) >= 16:
        masked_number = f"{'*' * 4} {'*' * 4} {'*' * 3} {'*' * 2} {'*' * 6} {number[-4:]}"

    return f"{prefix} {masked_number}"

else:
raise ValueError("Invalid input format")


def get_date(iso_date_str):
    """ Преобразует ISO-дату в удобный формат ДД.ММ.ГГГГ. :param iso_date_str: Дата в виде строки, например '2024-03-11T02:26:18.671407'. :return: Форматированная дата в виде '11.03.2024'. """
    date_obj = datetime.fromisoformat(iso_date_str)
    return date_obj.strftime("%d.%m.%Y")



