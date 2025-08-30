from typing import Union


def get_mask_card_number(card_number: int) -> str:
    """ Маскирует номер  карты формата ХХХХ ХХ** **** ХХХХ, оставляя видимым первые шесть и последние четыре цифры. """
    card_str = str(card_number)
    if len(card_str) != 16 or not card_str.isdigit():
        raise ValueError("Неверный формат номера карты")

    masked_part = "*" * 8
    return f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"


def get_mask_account(account_number: Union[int, str]) -> str:
    """ Маскирует банковский счет формата **ХХХХ, отображая лишь последние четыре цифры счета. """
    acc_str = str(account_number)
    if len(acc_str) < 4 or not acc_str.isdigit():
        raise ValueError("Неверный формат номера счёта")
    return f"**{acc_str[-4:]}"

