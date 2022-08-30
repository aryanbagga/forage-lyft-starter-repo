from abc import ABC

from MainCode.Tire.tire import Tire


class OctoprimeTire(Tire, ABC):
    def __init__(self, tire_wear):
        super().__init__()
        self.tire_wear = tire_wear

    def needs_service(self):
        tire_sum = 0
        for x in range(4):
            tire_sum += self.tire_wear[x]
        return tire_sum >= 3
