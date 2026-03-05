import unittest
from src.aeroplanes import Aircraft

class TestAircraft(unittest.TestCase):

    def test_initialization(self):
        # Тестируем корректную инициализацию
        aircraft = Aircraft("USA", "A123", 900, 10000)
        self.assertEqual(aircraft.registration_country, "USA")
        self.assertEqual(aircraft.callsign, "A123")
        self.assertEqual(aircraft.velocity, 900)
        self.assertEqual(aircraft.altitude, 10000)

    def test_invalid_registration_country(self):
        # Тестируем инициализацию с пустой страной регистрации
        with self.assertRaises(ValueError):
            Aircraft("", "A123", 900, 10000)

    def test_invalid_callsign(self):
        # Тестируем инициализацию с пустым позывным
        with self.assertRaises(ValueError):
            Aircraft("USA", "", 900, 10000)

    def test_invalid_velocity(self):
        # Тестируем инициализацию с отрицательной скоростью
        with self.assertRaises(ValueError):
            Aircraft("USA", "A123", -100, 10000)

    def test_invalid_altitude(self):
        # Тестируем инициализацию с отрицательной высотой
        with self.assertRaises(ValueError):
            Aircraft("USA", "A123", 900, -1000)

    def test_comparison_lt(self):
        # Тестируем оператор <
        aircraft1 = Aircraft("USA", "A123", 800, 10000)
        aircraft2 = Aircraft("USA", "A124", 900, 10000)
        self.assertTrue(aircraft1 < aircraft2)
        self.assertFalse(aircraft2 < aircraft1)

    def test_comparison_eq(self):
        # Тестируем оператор ==
        aircraft1 = Aircraft("USA", "A123", 900, 10000)
        aircraft2 = Aircraft("USA", "A124", 900, 10000)
        self.assertTrue(aircraft1 == aircraft2)

    def test_comparison_le(self):
        # Тестируем оператор <=
        aircraft1 = Aircraft("USA", "A123", 800, 10000)
        aircraft2 = Aircraft("USA", "A124", 900, 10000)
        self.assertTrue(aircraft1 <= aircraft2)
        self.assertTrue(aircraft1 <= aircraft1)

if __name__ == '__main__':
    unittest.main()
