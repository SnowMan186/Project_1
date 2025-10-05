import pytest

from src.bank_processing import process_bank_search


@pytest.fixture
def sample_transactions():
    return [
        {"id": 1, "description": "Перечисление зарплаты"},
        {"id": 2, "description": "Операция пополнения счёта"},
        {"id": 3, "description": "Оплата товаров онлайн"}
    ]


def test_process_bank_search(sample_transactions):
    results = process_bank_search(sample_transactions, "зарплата")
    assert len(results) == 0

