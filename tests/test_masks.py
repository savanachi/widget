import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "my_input, my_output",
    [
        ("1596837868705199", "1596 83** **** 5199"),
        ("71583007347267", "wrong datas"),
        ("7158300734726758", "7158 30** **** 6758"),
        ("715830073472675899", "wrong datas"),
    ],
)
def test_get_mask_card_number(my_input, my_output):
    assert get_mask_card_number(my_input) == my_output


@pytest.mark.parametrize(
    "my_input, my_output",
    [
        ("64686473678894779589", "**9589"),
        ("646864736788947795", "wrong datas"),
        ("35383033474447895560", "**5560"),
        ("6468647367889477958999", "wrong datas"),
    ],
)
def test_get_mask_account(my_input, my_output):
    assert get_mask_account(my_input) == my_output
