def filter_aeroplanes(aeroplanes, filter_words):
    """
    Фильтрует самолеты по странам регистрации.

    """
    filtered_aeroplanes = [
        aircraft for aircraft in aeroplanes
        if aircraft['registration_country'] in filter_words
    ]
    return filtered_aeroplanes


def parse_altitude_range(altitude_range):
    """
    Парсит строку диапазона высот в кортеж двух чисел.

    """
    try:
        min_altitude, max_altitude = map(int, altitude_range.split('-'))
        return min_altitude, max_altitude
    except ValueError:
        raise ValueError("Диапазон высот должен быть в формате 'min - max'.")


def get_aeroplanes_by_altitude(filtered_aeroplanes, altitude_range):
    """
    Фильтрует самолеты по диапазону высот.

    """
    min_altitude, max_altitude = parse_altitude_range(altitude_range)

    ranged_aeroplanes = [
        aircraft for aircraft in filtered_aeroplanes
        if min_altitude <= aircraft['altitude'] <= max_altitude
    ]
    return ranged_aeroplanes


def sort_aeroplanes(ranged_aeroplanes):
    """
    Сортирует самолеты по высоте от большей к меньшей.

    """
    sorted_aeroplanes = sorted(ranged_aeroplanes, key=lambda aircraft: aircraft['altitude'], reverse=True)
    return sorted_aeroplanes


def get_top_aeroplanes(sorted_aeroplanes, top_n):
    """
    Возвращает топ N самолетов из отсортированного списка.

    """
    return sorted_aeroplanes[:top_n]


def print_aeroplanes(top_aeroplanes):
    """
    Печатает информацию о самолетах: страна регистрации, позывной рейса, горизонтальная скорость, высота.

    """
    for index, aircraft in enumerate(top_aeroplanes, start=1):
        print(f"Самолет {index}:")
        print(f"  Страна регистрации: {aircraft['registration_country']}")
        print(f"  Позывной рейса: {aircraft['callsign']}")
        print(f"  Горизонтальная скорость: {aircraft['velocity']} м/с")
        print(f"  Высота: {aircraft['altitude']} м")
        print()
