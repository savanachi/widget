from src.widget import mask_account_card


def test_mask_account_card(account_card_datas):
    mask_account_card(bank_accounts= account_card_datas)
