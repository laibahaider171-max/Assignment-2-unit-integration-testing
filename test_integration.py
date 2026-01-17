import pytest
from bank_app import transfer, calculate_interest

def test_transfer_success():
    from_balance, to_balance = transfer(5000, 2000, 1000)
    assert from_balance == 4000
    assert to_balance == 3000

def test_transfer_insufficient_balance():
    with pytest.raises(ValueError):
        transfer(1000, 2000, 3000)

def test_transfer_and_interest():
    from_balance, to_balance = transfer(10000, 2000, 2000)
    updated_balance = calculate_interest(to_balance, 5, 1)
    assert updated_balance == pytest.approx(4200)
