class Aircraft:
    __slots__ = ('registration_country', 'callsign', 'velocity', 'altitude')

    def __init__(self, registration_country, callsign, velocity, altitude):
        self.registration_country = self.__validate_registration_country(registration_country)
        self.callsign = self.__validate_callsign(callsign)
        self.velocity = self.__validate_velocity(velocity)
        self.altitude = self.__validate_altitude(altitude)

    def __validate_registration_country(self, registration_country):
        # Проверка корректности страны регистрации (например, не пустая строка)
        if not registration_country:
            raise ValueError("Страна регистрации не может быть пустой")
        return registration_country

    def __validate_callsign(self, callsign):
        # Проверка корректности позывного (например, не пустая строка)
        if not callsign:
            raise ValueError("Позывной не может быть пустым")
        return callsign

    def __validate_velocity(self, velocity):
        # Проверка корректности скорости (например, положительное число)
        if velocity < 0:
            raise ValueError("Скорость не может быть отрицательной")
        return velocity

    def __validate_altitude(self, altitude):
        # Проверка корректности высоты (например, положительное число)
        if altitude < 0:
            raise ValueError("Высота не может быть отрицательной")
        return altitude

    def __lt__(self, other):
        # Сравнение самолетов по высоте для оператора <
        return self.altitude < other.altitude

    def __eq__(self, other):
        # Сравнение самолетов по высоте для оператора ==
        return self.altitude == other.altitude

    def __le__(self, other):
        # Сравнение самолетов по высоте для оператора <=
        return self.altitude <= other.altitude

    def __str__(self):
        return f"Aircraft {self.callsign}: {self.velocity} m/s, {self.altitude} m, {self.registration_country}"
