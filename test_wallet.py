from mywallet import Wallet
from mywallet import NotEnoughMoney

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

def test_wallet_credit_increses_balance():
    wallet = Wallet (100)
    # exercise
    wallet.credit(40)
    assert wallet.balance() == 140

def test_wallet_debit_decreses_balance():
    wallet = Wallet(100)
    wallet.debit(80)
    assert wallet.balance() == 20

def test_wallet_debit_more_than_balace_raise_error():
    wallet = Wallet(100)
    error = False
    try:
        wallet.debit(500)
    except NotEnoughMoney:
        error = True
    assert error
