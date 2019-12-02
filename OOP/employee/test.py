from employee import Employee
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
