players = [
    {'name': 'Антон', 'last name': 'Бирюков', 'raiting': 9},
    {'name': 'Алексей', 'last name': 'Бодня', 'raiting': 10},
    {'name': 'Федор', 'last name': 'Сидоров', 'raiting': 4},
    {'name': 'Михаил', 'last name': 'Семенов', 'raiting': 6}
]


def sort_by_lastname(iterable):
    """Сортировка по фамилии (по алфавиту)"""
    return sorted(iterable, key=lambda x: x['last name'])


def sort_by_raitings(iterable, from_best_score_to_lose=False):
    """
    Сортировка по рейтингу.
    
    Args:
        iterable: список словарей с игроками
        from_best_score_to_lose: если True — от лучшего к худшему
    
    Returns:
        Отсортированный список
    """
    if from_best_score_to_lose:
        return sorted(iterable, key=lambda x: x['raiting'], reverse=True)
    else:
        return sorted(iterable, key=lambda x: x['raiting'], reverse=False)


def start_program():
    """Запуск интерактивной программы сортировки"""
    while True:
        message_input = input(
            "\nВыберите вариант сортировки:\n"
            "1. По фамилии (А-Я)\n"
            "2. По рейтингу (от худшего к лучшему)\n"
            "3. По рейтингу (от лучшего к худшему)\n"
            "Введите число (1-3): "
        )

        try:
            num = int(message_input)
            if num < 1 or num > 3:
                print('Нужно выбрать число от 1 до 3.')
                continue
            break
        except ValueError:
            print("Ошибка: введите число от 1 до 3.")

    if num == 1:
        result = sort_by_lastname(players)
        print("\nРезультат (по фамилии):")
        for player in result:
            print(f"{player['name']} {player['last name']} — {player['raiting']}")

    elif num == 2:
        result = sort_by_raitings(players)
        print("\nРезультат (по рейтингу, от худшего к лучшему):")
        for player in result:
            print(f"{player['name']} {player['last name']} — {player['raiting']}")

    elif num == 3:
        result = sort_by_raitings(players, from_best_score_to_lose=True)
        print("\nРезультат (по рейтингу, от лучшего к худшему):")
        for player in result:
            print(f"{player['name']} {player['last name']} — {player['raiting']}")


if __name__ == "__main__":
    start_program()