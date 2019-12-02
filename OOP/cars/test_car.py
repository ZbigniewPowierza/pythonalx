from car import ElectricCar

class TestCars:

    def test_init(self):
        ecar = ElectricCar(100)
        assert ecar.zasieg == 100

    def test_drive_below_zasieg(self):
        ecar = ElectricCar(100)
        ecar.drive(70)
        assert ecar.drive == 70

    def test_charge(self): # używam (self), bo mam zdefiniowaną klasę, gdyby było bez klasy wówczas byłoby ()
        ecar = ElectricCar (100)