from abc import ABC
from MainCode.Servicable import Serviceable


class Car(Serviceable, ABC):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()

