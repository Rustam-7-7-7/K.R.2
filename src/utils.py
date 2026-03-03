def filter_aeroplanes(aeroplanes, filter_words):
    """
    Фильтрует самолеты по странам регистрации.

    """
    filtered_aeroplanes = [
        aircraft for aircraft in aeroplanes
        if aircraft['registration_country'] in filter_words
    ]
    return filtered_aeroplanes


