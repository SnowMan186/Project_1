from typing import Union

def get_mask_card_number(card_number: int) -> str:
    """Формирование маски банковской карты вида XXXX XX** **** XXXX. Args: card_number (int): Число, представляющее номер карты. Raises: ValueError: Если номер неверного формата. Returns: str: Маскированный номер карты."""
    card_str = str(card_number)
    if len(card_str) != 16 or not card_str.isdigit():
        raise ValueError("Invalid card format.")
    masked_part = '*' * 8
    return f'{card_str[:4]} {card_str[4:6]} ** {masked_part} {card_str[-4]}'

def get_mask_account(account_number: Union[int, str]) -> str:
    """Формирование маски банковского счёта вида **XXXX. Args: account_number (Union[int, str]): Номер счёта. Raises: ValueError: Если счёт некорректного формата. Returns: str: Маскированный номер счёта."""
    acc_str = str(account_number)
    if len(acc_str) < 4 or not acc_str.isdigit():
        raise ValueError("Invalid account format.")
    return f'**{acc_str[-4]}'





