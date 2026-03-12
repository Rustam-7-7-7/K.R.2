from abc import ABC, abstractmethod
import json
import os


# Абстрактный класс для работы с файлами
class AbstractFileHandler(ABC):

    @abstractmethod
    def add_aircraft(self, aircraft):
        """Добавляет информацию о самолете в файл."""
        pass

    @abstractmethod
    def get_aircrafts(self, criteria=None):
        """Получает данные из файла по указанным критериям."""
        pass

    @abstractmethod
    def delete_aircraft(self, aircraft_id):
        """Удаляет информацию о самолете."""
        pass


# Класс для работы с JSON-файлами
class JSONFileHandler(AbstractFileHandler):

    def __init__(self, filename='aircrafts.json'):
        self._filename = filename  # Приватный атрибут с именем файла
        # Если файла не существует, создаем пустой файл
        if not os.path.exists(self._filename):
            with open(self._filename, 'w') as file:
                json.dump([], file)

    def add_aircraft(self, aircraft):
        with open(self._filename, 'r') as file:
            data = json.load(file)

        # Проверка на дублирование
        if aircraft not in data:
            data.append({
                'registration_country': aircraft.registration_country,
                'callsign': aircraft.callsign,
                'velocity': aircraft.velocity,
                'altitude': aircraft.altitude
            })
            with open(self._filename, 'w') as file:
                json.dump(data, file)

    def get_aircrafts(self, criteria=None):
        with open(self._filename, 'r') as file:
            data = json.load(file)
        # Здесь можно добавить фильтрацию данных по критериям, если нужно
        return data

    def delete_aircraft(self, aircraft_id):
        with open(self._filename, 'r') as file:
            data = json.load(file)

        # Удаление записи по ID (например, по уникальному callsign)
        data = [aircraft for aircraft in data if aircraft['callsign'] != aircraft_id]

        with open(self._filename, 'w') as file:
            json.dump(data, file)


# Пример использования класса Aircraft
class Aircraft:
    def __init__(self, registration_country, callsign, velocity, altitude):
        self.registration_country = registration_country
        self.callsign = callsign
        self.velocity = velocity
        self.altitude = altitude
