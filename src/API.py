from abc import ABC, abstractmethod
from requests import get, RequestException


class AbstractAPIClient(ABC):

    @abstractmethod
    def _connect(self, url, params=None, headers=None):
        """Подключается к API и возвращает ответ."""
        pass

    @abstractmethod
    def get_aeroplanes(self, country: str):
        """Получает информацию о самолетах по названию страны."""
        pass


class APIAdapter(AbstractAPIClient):

    def __init__(self) -> None:
        self.__openstreetmap_url = 'https://nominatim.openstreetmap.org/search'
        self.__opensky_url = 'https://opensky-network.org/api/states/all?'
        self.__aeroplanes = None

    def _connect(self, url, params=None, headers=None):
        """Подключается к API и возвращает ответ."""
        try:
            response = get(url=url, params=params, headers=headers)
            response.raise_for_status()  # Проверка успешности ответа
            return response.json()
        except RequestException as e:
            print(f"Произошла ошибка при запросе API: {e}")
            return None

    def get_aeroplanes(self, country: str):
        """Получает информацию о самолетах по названию страны."""
        headers_nominatim = {
            'User-Agent': 'test-app/1.0',
        }

        params_nominatim = {
            'country': country,
            'format': 'json',
            'limit': 1,
        }

        # Подключение к OpenStreetMap API
        data = self._connect(self.__openstreetmap_url, params=params_nominatim, headers=headers_nominatim)

        if not data:
            print(f"Не удалось найти данные для страны: {country}")
            return

        geo_coordinates = data[0].get('boundingbox')

        if not geo_coordinates:
            print(f"Не удалось получить координаты для страны: {country}")
            return

        params_opensky = {
            'lamin': geo_coordinates[0],
            'lamax': geo_coordinates[1],
            'lomin': geo_coordinates[2],
            'lomax': geo_coordinates[3],
        }

        # Подключение к OpenSky API
        self.__aeroplanes = self._connect(self.__opensky_url, params=params_opensky)

        if self.__aeroplanes and 'states' in self.__aeroplanes:
            print(f"Найдено {len(self.__aeroplanes['states'])} самолетов в воздушном пространстве {country}:")
            return self.__aeroplanes
        else:
            print(f"Нет данных о самолетах в воздушном пространстве {country}.")
