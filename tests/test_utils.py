import unittest
from src.utils import filter_aeroplanes, parse_altitude_range, get_aeroplanes_by_altitude, sort_aeroplanes, get_top_aeroplanes

class TestAircraftFunctions(unittest.TestCase):

    def setUp(self):
        # Данные для тестов
        self.aeroplanes = [
            {'registration_country': 'USA', 'callsign': 'A123', 'velocity': 900, 'altitude': 10000},
            {'registration_country': 'Canada', 'callsign': 'B456', 'velocity': 850, 'altitude': 9000},
            {'registration_country': 'USA', 'callsign': 'C789', 'velocity': 920, 'altitude': 11000}
        ]

    def test_filter_aeroplanes(self):
        # Тестируем фильтрацию по странам
        result = filter_aeroplanes(self.aeroplanes, ['USA'])
        self.assertEqual(len(result), 2)
        self.assertTrue(all(aircraft['registration_country'] == 'USA' for aircraft in result))

    def test_parse_altitude_range(self):
        # Тестируем парсинг диапазона высот
        result = parse_altitude_range("5000 - 15000")
        self.assertEqual(result, (5000, 15000))

        # Тестируем некорректный формат
        with self.assertRaises(ValueError):
            parse_altitude_range("invalid range")

    def test_get_aeroplanes_by_altitude(self):
        # Тестируем фильтрацию по высоте
        filtered_aeroplanes = filter_aeroplanes(self.aeroplanes, ['USA', 'Canada'])
        result = get_aeroplanes_by_altitude(filtered_aeroplanes, "9000 - 11000")
        self.assertEqual(len(result), 3)

        result = get_aeroplanes_by_altitude(filtered_aeroplanes, "9500 - 10500")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['callsign'], 'A123')

    def test_sort_aeroplanes(self):
        # Тестируем сортировку по высоте
        filtered_aeroplanes = filter_aeroplanes(self.aeroplanes, ['USA', 'Canada'])
        ranged_aeroplanes = get_aeroplanes_by_altitude(filtered_aeroplanes, "5000 - 15000")
        result = sort_aeroplanes(ranged_aeroplanes)
        self.assertEqual(result[0]['altitude'], 11000)
        self.assertEqual(result[1]['altitude'], 10000)
        self.assertEqual(result[2]['altitude'], 9000)

    def test_get_top_aeroplanes(self):
        # Тестируем получение топ N самолетов
        sorted_aeroplanes = sort_aeroplanes(self.aeroplanes)
        result = get_top_aeroplanes(sorted_aeroplanes, 2)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['callsign'], 'C789')
        self.assertEqual(result[1]['callsign'], 'A123')

if __name__ == '__main__':
    unittest.main()
