import pytest

from src.widget import mask_account_card, get_date


def test_mask_account_card():
    assert mask_account_card(bank_accounts= 'Maestro 1596837868705199') == 'Maestro 1596 83** **** 5199'
    assert mask_account_card(bank_accounts='\n') == 'empty string'
    assert mask_account_card(bank_accounts= 'fassdfa daSDSA') == 'wrong data'
    assert mask_account_card(bank_accounts='Счет 64686473678894779589') == 'Счет **9589'


@pytest.fixture
def date():
    return "2024-03-11T02:26:18.671407"


def test_get_date(date):
    assert get_date(date) == "11.03.2024"
