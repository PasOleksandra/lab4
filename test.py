import unittest
import os
import json
from lab2 import Meter, MeterManager  # Replace `your_module` with the name of your Python file (without .py)


class TestMeter(unittest.TestCase):
    def test_initialization(self):
        meter = Meter(id="123", type="electric", initial_reading=100)
        self.assertEqual(meter.id, "123")
        self.assertEqual(meter.type, "electric")
        self.assertEqual(meter.get_reading(), 100)

    def test_update_reading_valid(self):
        meter = Meter(id="123", type="electric", initial_reading=100)
        meter.update_reading(150)
        self.assertEqual(meter.get_reading(), 150)

    def test_update_reading_invalid(self):
        meter = Meter(id="123", type="electric", initial_reading=100)
        with self.assertRaises(ValueError):
            meter.update_reading(50)


class TestMeterManager(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_meters.json"
        self.manager = MeterManager(filename=self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_meter(self):
        meter = Meter(id="123", type="electric", initial_reading=100)
        self.manager.add_meter(meter)

        self.assertIn("123", self.manager.meters)
        self.assertEqual(self.manager.meters["123"]["type"], "electric")
        self.assertEqual(self.manager.meters["123"]["reading"], 100)

    def test_update_meter_valid(self):
        meter = Meter(id="123", type="electric", initial_reading=100)
        self.manager.add_meter(meter)
        self.manager.update_meter("123", 200)

        self.assertEqual(self.manager.meters["123"]["reading"], 200)

    def test_update_meter_invalid(self):
        with self.assertRaises(KeyError):
            self.manager.update_meter("999", 200)

    def test_get_meter_reading_valid(self):
        meter = Meter(id="123", type="electric", initial_reading=100)
        self.manager.add_meter(meter)
        reading = self.manager.get_meter_reading("123")

        self.assertEqual(reading, 100)

    def test_get_meter_reading_invalid(self):
        with self.assertRaises(KeyError):
            self.manager.get_meter_reading("999")

    def test_persistence(self):
        meter = Meter(id="123", type="electric", initial_reading=100)
        self.manager.add_meter(meter)

        # Reload the manager and check data persistence
        new_manager = MeterManager(filename=self.test_file)
        self.assertIn("123", new_manager.meters)
        self.assertEqual(new_manager.meters["123"]["type"], "electric")
        self.assertEqual(new_manager.meters["123"]["reading"], 100)


if __name__ == "__main__":
    unittest.main()
