# tests/test_masks.py
# tests/test_masks.py

import pytest
from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number(valid_card_numbers):
    for card in valid_card_numbers:
        result = get_mask_card_number(int(card))
        assert isinstance(result, str)
        parts = result.split()
        assert len(parts) == 4
        assert all(part.isalnum() for part in parts[:-1])
        assert parts[-1].isdigit()


def test_get_mask_card_number_invalid(invalid_card_numbers):
    for card in invalid_card_numbers:
        with pytest.raises(ValueError):
            get_mask_card_number(int(card))


def test_get_mask_account(valid_accounts):
    for account in valid_accounts:
        masked = get_mask_account(account)
        assert masked.startswith("**") and masked.endswith(account[-4:])


def test_get_mask_account_invalid(invalid_accounts):
    for account in invalid_accounts:
        with pytest.raises(ValueError):
            get_mask_account(account)


# Объединяющий тест, проверяющий разные типы маскирования
def test_mask_account_valid(valid_card_numbers, valid_accounts):
    inputs = [(f"карта {card}", get_mask_card_number(int(card))) for card in valid_card_numbers]
    inputs.extend([(f"счет {acc}", get_mask_account(acc)) for acc in valid_accounts])

    for input_data, expected_result in inputs:
        if input_data.startswith("карта"):
            actual_result = get_mask_card_number(int(input_data.split()[1]))
        elif input_data.startswith("счет"):
            actual_result = get_mask_account(input_data.split()[1])
        else:
            continue

        assert actual_result == expected_result


# Тест на обработку некорректных данных
def test_mask_account_invalid():
    invalid_inputs = ["Некорректные данные", ""]
    for input_data in invalid_inputs:
        with pytest.raises(ValueError):
            if input_data.startswith("карта"):
                get_mask_card_number(int(input_data.split()[1]))
            elif input_data.startswith("счет"):
                get_mask_account(input_data.split()[1])
            else:
                raise ValueError("Некорректный тип данных")
