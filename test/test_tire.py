import unittest
from datetime import date

from MainCode.Tire.octoprime_tire import OctoprimeTire
from MainCode.Tire.carrigan_tire import CarriganTire


class TestOctoprimeTire(unittest.TestCase):
    def test_needs_service_true(self):
        tire = OctoprimeTire([0.8, 0.8, 0.8, 0.8])
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire = OctoprimeTire([0.7, 0.7, 0.7, 0.7])
        self.assertFalse(tire.needs_service())


class TestCarriganTire(unittest.TestCase):
    def test_needs_service_true(self):
        tire = CarriganTire([0.1, 0.1, 0.1, 0.91])
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire = CarriganTire([0.7, 0.7, 0.7, 0.7])
        self.assertFalse(tire.needs_service())
