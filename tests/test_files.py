import unittest
import os
import json
from src.files import JSONFileHandler, Aircraft

class TestJSONFileHandler(unittest.TestCase):

    def setUp(self):
        # Создаем временный файл для тестирования
        self.test_filename = 'test_aircrafts.json'
        self.file_handler = JSONFileHandler(self.test_filename)

    def tearDown(self):
        # Удаляем временный файл после тестов
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_add_aircraft(self):
        # Тестируем добавление самолета
        aircraft = Aircraft("USA", "A123", 900, 10000)
        self.file_handler.add_aircraft(aircraft)

        with open(self.test_filename, 'r') as file:
            data = json.load(file)

        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['callsign'], "A123")

    def test_get_aircrafts(self):
        # Тестируем получение данных о самолетах
        aircraft1 = Aircraft("USA", "A123", 900, 10000)
        aircraft2 = Aircraft("Canada", "B456", 850, 9000)
        self.file_handler.add_aircraft(aircraft1)
        self.file_handler.add_aircraft(aircraft2)

        data = self.file_handler.get_aircrafts()
        self.assertEqual(len(data), 2)

    def test_delete_aircraft(self):
        # Тестируем удаление самолета
        aircraft1 = Aircraft("USA", "A123", 900, 10000)
        aircraft2 = Aircraft("Canada", "B456", 850, 9000)
        self.file_handler.add_aircraft(aircraft1)
        self.file_handler.add_aircraft(aircraft2)

        self.file_handler.delete_aircraft("A123")

        data = self.file_handler.get_aircrafts()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['callsign'], "B456")

if __name__ == '__main__':
    unittest.main()
