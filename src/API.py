from abc import ABC, abstractmethod
from requests import get, RequestException


class AbstractAPIClient(ABC):

    @abstractmethod
    def get_aeroplanes(self, country: str) -> None:
        """Получает информацию о самолетах по названию страны."""
        pass


class APIAdapter(AbstractAPIClient):

    def __init__(self) -> None:
        self.openstreetmap_url = 'https://nominatim.openstreetmap.org/search'
        self.opensky_url = 'https://opensky-network.org/api/states/all?'
        self.aeroplanes = None

    def get_aeroplanes(self, country: str) -> None:
        headers_nominatim = {
            'User-Agent': 'test-app/1.0',
        }

        params_nominatim = {
            'country': country,
            'format': 'json',
            'limit': 1,
        }

        try:
            response = get(url=self.openstreetmap_url, params=params_nominatim, headers=headers_nominatim)
            response.raise_for_status()  # Проверка успешности ответа
            data = response.json()

            if not data:
                print(f"Не удалось найти данные для страны: {country}")
                return

            geo_coordinates = data[0].get('boundingbox')

            if not geo_coordinates:
                print(f"Не удалось получить координаты для страны: {country}")
                return

            params = {
                'lamin': geo_coordinates[0],
                'lamax': geo_coordinates[1],
                'lomin': geo_coordinates[2],
                'lomax': geo_coordinates[3],
            }

            response = get(url=self.opensky_url, params=params)
            response.raise_for_status()  # Проверка успешности ответа

            self.aeroplanes = response.json()

            if self.aeroplanes and 'states' in self.aeroplanes:
                print(f"Найдено {len(self.aeroplanes['states'])} самолетов в воздушном пространстве {country}:")
                # for state in self.aeroplanes['states']:
                #     print(state)
                return self.aeroplanes
            else:
                print(f"Нет данных о самолетах в воздушном пространстве {country}.")

        except RequestException as e:
            print(f"Произошла ошибка при запросе API: {e}")
