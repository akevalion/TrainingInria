from mywallet import Wallet
from mywallet import NotEnoughMoney
from mywallet import NegativeAmountError
import pytest
import unittest
class TestSomeThing (unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()
    
    def test_something(self):
        self.assertTrue(True)

    def tearDown(self) -> None:
        return super().tearDown()

def test_wallet_balance_is_zero():
    # setup
    wallet = Wallet()
    # check expectations
    assert wallet.balance() == 0

def test_wallet_initialize_with_money():
    # setup
    wallet = Wallet(100)
    # check expectations
    assert wallet.balance() == 100

def test_wallet_credit_with_negative_amount_fails():
    # setup
    wallet = Wallet ()
    # exercise
    with pytest.raises(NegativeAmountError):
        wallet.credit(-40)
    assert wallet.balance() == 0

def test_wallet_debit_decreses_balance():
    # setup
    wallet = Wallet(100)
    # exercise
    wallet.debit(80)
    # check expectations
    assert wallet.balance() == 20

def test_debit_balance_with_not_enough_founds_fails():
    # setup
    wallet = Wallet()
    # exercise
    # check expectations
    with pytest.raises(NotEnoughMoney):
        wallet.debit(300)
    assert wallet.balance() == 0

def test_wallet_debit_more_than_balace_raise_error():
    # setup
    wallet = Wallet(100)
    # exercise
    error = False
    try:
        wallet.debit(500)
    except NotEnoughMoney:
        error = True
    # check expectations
    assert error
    assert wallet.balance() == 100
