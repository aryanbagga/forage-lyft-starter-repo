from datetime import date

from MainCode.Battery.nubbin_battery import NubbinBattery
from MainCode.Battery.spindler_battery import SpindlerBattery
from MainCode.car import Car
from MainCode.engine.capulet_engine import CapuletEngine
from MainCode.engine.sternman_engine import SternmanEngine
from MainCode.engine.willoughby_engine import WilloughbyEngine


class CarFactory:

    @staticmethod
    def create_calliope(current_date: date, last_service_date: date,
                        current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        new_car = Car(engine, battery)
        return new_car

    @staticmethod
    def create_glissade(current_date: date, last_service_date: date,
                        current_mileage: int, last_service_mileage: int) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        new_car = Car(engine, battery)
        return new_car

    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date,
                          warning_light_on: bool) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(current_date, last_service_date)
        new_car = Car(engine, battery)
        return new_car

    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date,
                         current_mileage: int,
                         last_service_mileage: int) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        new_car = Car(engine, battery)
        return new_car

    @staticmethod
    def create_thovex(current_date: date, last_service_date: date,
                      current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        new_car = Car(engine, battery)
        return new_car
