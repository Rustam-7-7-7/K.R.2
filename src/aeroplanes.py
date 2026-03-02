class Aircraft:
    def __init__(self, registration_country, callsign, velocity, altitude):
        self.registration_country = self.validate_registration_country(registration_country)
        self.callsign = self.validate_callsign(callsign)
        self.velocity = self.validate_velocity(velocity)
        self.altitude = self.validate_altitude(altitude)

    def validate_registration_country(self, registration_country):
        # Проверка корректности страны регистрации (например, не пустая строка)
        if not registration_country:
            raise ValueError("Страна регистрации не может быть пустой")
        return registration_country

    def validate_callsign(self, callsign):
        # Проверка корректности позывного (например, не пустая строка)
        if not callsign:
            raise ValueError("Позывной не может быть пустым")
        return callsign

    def validate_velocity(self, velocity):
        # Проверка корректности скорости (например, положительное число)
        if velocity < 0:
            raise ValueError("Скорость не может быть отрицательной")
        return velocity

    def validate_altitude(self, altitude):
        # Проверка корректности высоты (например, положительное число)
        if altitude < 0:
            raise ValueError("Высота не может быть отрицательной")
        return altitude

    def __lt__(self, other):
        # Сравнение самолетов по скорости для оператора <
        return self.velocity < other.velocity

    def __eq__(self, other):
        # Сравнение самолетов по скорости для оператора ==
        return self.velocity == other.velocity

    def __le__(self, other):
        # Сравнение самолетов по скорости для оператора <=
        return self.velocity <= other.velocity

    def __str__(self):
        return f"Aircraft {self.callsign}: {self.velocity} m/s, {self.altitude} m, {self.registration_country}"
