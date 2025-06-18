import pytest
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions

def test_card_number_generator():
    card_number_generator()


def test_filter_by_currency():
    filter_by_currency()


def test_transaction_descriptions():
    transaction_descriptions()