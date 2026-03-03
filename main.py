from src.API import APIAdapter
from src.files import JSONFileHandler, Aircraft


# Функция для взаимодействия с пользователем
def user_interaction():
    country = input("Введите название страны: ")
    api = APIAdapter()
    file_handler = JSONFileHandler()

    # Получаем данные о самолетах
    aeroplanes_data = api.get_aeroplanes(country)

    if aeroplanes_data and 'states' in aeroplanes_data:
        # Обрабатываем каждую запись о самолете
        for state in aeroplanes_data['states']:
            # Создаем объект Aircraft
            aircraft = Aircraft(
                registration_country=state[2],
                callsign=state[1].strip(),
                velocity=state[9],
                altitude=state[7] if state[7] is not None else 0  # Используем 0 если высота неизвестна
            )
            # Добавляем объект в файл
            file_handler.add_aircraft(aircraft)
        print("Данные о самолетах успешно записаны в файл.")
    else:
        print("Нет данных о самолетах для записи.")

    aeroplanes = file_handler.get_aircrafts()


    top_n = int(input("Введите количество самолетов для вывода в топ N: "))
    filter_words = input("Введите названия стран для фильтрации по стране регистрации: ").split()
    altitude_range = input("Введите диапазон высот полета: ") # Пример: 100000 - 150000

    from src.utils import filter_aeroplanes

    filtered_aeroplanes = filter_aeroplanes(aeroplanes, filter_words)

    ranged_aeroplanes = get_aeroplanes_by_altitude(filtered_aeroplanes, altitude_range)

    sorted_aeroplanes = sort_aeroplanes(ranged_aeroplanes)
    top_aeroplanes = get_top_aeroplanes(sorted_aeroplanes, top_n)
    print_aeroplanes(top_aeroplanes)


if __name__ == "__main__":
    user_interaction()
