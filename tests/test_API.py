import unittest
from unittest.mock import patch, MagicMock
from requests import RequestException
from src.API import APIAdapter


class TestAPIAdapter(unittest.TestCase):

    @patch('src.API.get')
    def test_get_aeroplanes_success(self, mock_get):
        # Мокаем успешный ответ от OpenStreetMap и OpenSky Network
        mock_osm_response = MagicMock()
        mock_osm_response.json.return_value = [{'boundingbox': [1, 2, 3, 4]}]
        mock_osm_response.status_code = 200

        mock_opensky_response = MagicMock()
        mock_opensky_response.json.return_value = {
            'states': [['call1', 'country1', 0, 0, 0, 0, 0, 100, False, 200, 0, 0, None, 0, 'squawk', False, 0]]}
        mock_opensky_response.status_code = 200

        mock_get.side_effect = [mock_osm_response, mock_opensky_response]

        api_adapter = APIAdapter()
        result = api_adapter.get_aeroplanes('TestCountry')

        self.assertIsNotNone(result)
        self.assertIn('states', result)
        self.assertEqual(len(result['states']), 1)
        self.assertEqual(result['states'][0][7], 100)  # Проверяем высоту

    @patch('src.API.get')
    def test_get_aeroplanes_no_data(self, mock_get):
        # Мокаем ответ без данных от OpenStreetMap
        mock_osm_response = MagicMock()
        mock_osm_response.json.return_value = []
        mock_osm_response.status_code = 200

        mock_get.return_value = mock_osm_response

        api_adapter = APIAdapter()
        result = api_adapter.get_aeroplanes('TestCountry')

        self.assertIsNone(result)

    @patch('src.API.get')
    def test_get_aeroplanes_error(self, mock_get):
        # Мокаем ошибку в ответе
        mock_get.side_effect = RequestException("API Error")

        api_adapter = APIAdapter()
        result = api_adapter.get_aeroplanes('TestCountry')

        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
