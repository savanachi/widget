from src.widget import mask_account_card


def test_mask_account_card():
    assert mask_account_card(bank_accounts= 'Maestro 1596837868705199') == 'Maestro 1596 83** **** 5199'
    assert mask_account_card(bank_accounts='\n') == 'empty string'
    assert mask_account_card(bank_accounts= 'fassdfa daSDSA') == 'wrong data'
    assert mask_account_card(bank_accounts='Счет 64686473678894779589') == 'Счет **9589'


