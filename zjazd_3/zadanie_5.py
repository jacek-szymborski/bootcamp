def test_cash_machine_not_available():
    cash_machine = CashMachine()
    assert not cash_machine.is_available()

def test_cash_machine_is_available_after_put_money():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.is_available()

def test_withdraw_money():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.withdraw_money(150) == [100, 50]
    assert cash_machine.withdraw_money(150) == []

def test_cash_machine_wrong_amount():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.withdraw_money(90) == []

def test_cash_machine_order_matters():
    cash_machine = CashMachine()
    cash_machine.put_money([20, 20, 50, 50])
    assert cash_machine.withdraw_money(100) == [50, 50]

def test_sach_machine_is_not_avaialble_after_withdrawal_all_money():
    cash_machine = CashMachine()
    cash_machine.put_money([50, 50])
    cash_machine.withdraw_money(100) == [50, 50]
    assert not cash_machine.is_available()



class CashMachine:

    def __init__(self):
        self.bills = []

    def is_available(self):
        if self.bills: # != []
            return True
        else:
            return False

    def put_money(self, bills):
        self.bills.extend(bills)

    def withdraw_money(self, amount):
        bills_to_withdraw = []
        for bill in sorted(self.bills, reverse=True):
            if sum(bills_to_withdraw) + bill <= amount:
                bills_to_withdraw.append(bill)

        if sum(bills_to_withdraw) == amount:
            for bill in bills_to_withdraw:
                self.bills.remove(bill)
            return bills_to_withdraw
        return []
