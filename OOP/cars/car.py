class ElectricCar:
        def __init__(self, zasieg):
            self.counter = 0

        def can_move(self):
            return self.counter < self.__zasieg


