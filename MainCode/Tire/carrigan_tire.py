from abc import ABC

from MainCode.Tire.tire import Tire


class CarriganTire(Tire, ABC):
    def __init__(self, tire_wear):
        super().__init__()
        self.tire_wear = tire_wear

    def needs_service(self):
        for x in range(4):
            if self.tire_wear[x] >= 0.9:
                return True
        return False
