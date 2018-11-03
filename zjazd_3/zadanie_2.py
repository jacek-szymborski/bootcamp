# def test_Employee():
#     emp = Employee('Jan', 'Kowalski', 100.0)
#     assert emp.imie == 'Jan'
#     assert emp.nazwisko == 'Kowalski'
#     assert emp.stawka == 100.0
#
# def test_Empolyee_register_time():
#     pass
# def test_Employee_pay_salary():
#     pass

def test_company():
    emp = Employee('Jan', 'Kowalski', 100.0)
    emp.register_time(5)
    google = Company("google")

    assert emp.imie == 'Jan'
    assert emp.nazwisko == 'Kowalski'
    assert emp.stawka == 100.0



class Employee:

    def __init__(self, imie, nazwisko, stawka):
        self.wrk_hrs = 0
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka

    def register_time(self, hrs):
        self.wrk_hrs += hrs

    def pay_salary(self):
        if self.wrk_hrs > 8:
            to_pay = 8 * self.stawka + (self.wrk_hrs - 8) * 2 * self.stawka
        else:
            to_pay = self.wrk_hrs * self.stawka
        self.wrk_hrs = 0

        return to_pay

class PremiumEmployee(Employee):

    def __init__(self,imie, nazwisko, stawka):
        super().__init__(imie, nazwisko, stawka)
        #Employee.__init__(self, imie, nazwisko, stawka)
        self.bonus = 0

    def give_bonus(self, bonus):
        self.bonus = bonus

    def pay_salary(self):

        "Przykład użycia kodu metody z klasy nadrzędnej - funkcja super() "

        # if self.wrk_hrs > 8:
        #     to_pay = (8 * self.stawka + (self.wrk_hrs - 8) * 2 * self.stawka) + self.bonus
        # else:
        #     to_pay = self.wrk_hrs * self.stawka + self.bonus
        # self.wrk_hrs = 0
        to_pay = super().pay_salary()
        return to_pay + self.bonus

class Company:

    def __init__(self, name):
        self.name = name
        self.employees = set()

    def add_employee(self, employee):
        self.employees.add(employee)

    def size(self):
        len(self.employees)

    def pay_all_salary(self):
        sum_ = 0
        for e in self.employees:
            sum_ += e.pay_salary()
        return sum_

emp = PremiumEmployee('Jan','Kowalski',100.0)
emp.register_time(5)
emp.give_bonus(1000.0)
print(emp.pay_salary())

