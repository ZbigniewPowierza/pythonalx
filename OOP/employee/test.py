from employee import Employee, PremiumEmployee, AmountBonus, PercentBonus
class TestEmployee:

    def test_init(self):
        e = Employee("Jan", "Nowak", 100.0)
        # e2 = Employee ("Kazimierz", "Kowalski", 120)

        assert e.fname == "Jan"
        assert e.name == "Nowak"
        assert e.stawka == 100.0
        # assert e2.fname == "Kazimierz"
        # assert e2.name == "Kowalski"
    def test_register_time(self):
        e = Employee("Jan", "Nowak", 100)
        e.register_time(5)
        assert e.registered_hours == 5

    def test_pay_salary_over_hours(self):
        e = Employee("Jan", "Nowak", 100)
        e.register_time(10)
        assert e.pay_salary() == 1200

    def test_pay_salary_normal_hours(self):
        e = Employee("Jan", "Nowak", 100)
        e.register_time(5)
        assert e.pay_salary() == 500

    def test_pay_salary_without_registered_time(self):
        e = Employee("Jan", "Nowak", 100)
        assert e.pay_salary() == 0

    def test_pay_salary_twice_normal_hours(self):
        e = Employee("Jan", "Nowak", 100)
        e.register_time(5)
        assert e.pay_salary() == 500
        assert e.pay_salary () == 0

class TestPremiumEmployee:

    def test_init(self):
        e = PremiumEmployee("Jan", "Nowak", 100.0)
        # p2 = Employee ("Kazimierz", "Kowalski", 120)

        assert e.fname == "Jan"
        assert e.name == "Nowak"
        assert e.stawka == 100.0


    def test_register_time(self):
        e = PremiumEmployee ("Jan", "Nowak", 100)
        e.register_time (5)
        assert e.registered_hours == 5


    def test_pay_salary_over_hours(self):
        e = PremiumEmployee ("Jan", "Nowak", 100)
        e.register_time (10)
        assert e.pay_salary () == 1200

    def test_pay_salary_normal_hours(self):
        e = PremiumEmployee("Jan", "Nowak", 100)
        e.register_time(5)
        assert e.pay_salary() == 500

    def test_pay_salary_without_registered_time(self):
        e = PremiumEmployee("Jan", "Nowak", 100)
        assert e.pay_salary() == 0

    def test_pay_salary_twice_normal_hours(self):
        e = PremiumEmployee("Jan", "Nowak", 100)
        e.register_time(16)
        assert e.pay_salary() == 2400
        assert e.pay_salary() == 0

    def test_give_bonus(self):
        e = PremiumEmployee("Jan", "Nowak", 100)
        bonus = AmountBonus(1000)
        e.give_bonus(bonus)
        assert e.bonuses == [bonus]

    def test_give_bonus(self):
        e = PremiumEmployee("Jan", "Nowak", 100)
        bonus = AmountBonus(1000)
        e.give_bonus(bonus)
        assert e.bonuses == [bonus]

    def test_pay_salary_normal_hours_bonus(self):
        e = PremiumEmployee("Jan", "Nowak", 100)
        e.register_time(5)
        e.give_bonus(1000)
        assert e.pay_salary() == 1500

    def test_pay_salary_over_hours_bonus(self):
        e = PremiumEmployee ("Jan", "Nowak", 100)
        e.register_time (10)
        e.give_bonus(1000)
        assert e.pay_salary () == 2200

    def test_pay_salary_without_registered_time_bonus(self):
        e = PremiumEmployee("Jan", "Nowak", 100)
        e.give_bonus(1000)
        assert e.pay_salary() == 1000

    def test_pay_salary_twice_normal_hours_bonus(self):
        e = PremiumEmployee("Jan", "Nowak", 100)
        e.register_time(16)
        e.give_bonus(1000)
        assert e.pay_salary() == 3400
        assert e.pay_salary() == 0