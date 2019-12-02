class Employee:
    def __init__(self, fname, name, stawka):
        self.fname = fname
        self.name = name
        self.stawka = stawka
        self.registered_hours = 0 # zabawa z podwójnym podkreśleniem, chodzi o zmienne prywatne, jak zobaczysz jedno czy dwa podkreślenia to informacja dla odbiorcy kodu

    def register_time(self, time):
        self.registered_hours = time

    def pay_salary(self):
        if self.registered_hours <= 8:
            to_pay = self.registered_hours * self.stawka
        else:
            to_pay = 8 * self.stawka + (self.registered_hours - 8) * self.stawka * 2
        self.registered_hours = 0
        return to_pay

    def _pay_salary(self): # to oznacza że ta metoda moze się zmienić, zniknąć, użytkownik wtedy wie dzięki podkreśleniu, że to nie jest metoda pubiczna
        pass

    # def show(self):
    #     return f"{self.name} ({self.fname}), stawka: {self.stawka}"
