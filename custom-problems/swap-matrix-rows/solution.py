from random import randint

def create_matrix():
    """Создаёт матрицу 6×6 со случайными числами от 0 до 10."""
    return [[randint(0, 10) for _ in range(6)] for _ in range(6)]

def print_matrix(matrix):
    """Выводит матрицу в виде таблицы."""
    for row in matrix:
        for num in row:
            print(f"{num:2}", end="\t")
        print()

def swap_rows(matrix):
    """
    Возвращает новую матрицу, в которой:
    - 1-я и 2-я строки поменяны местами,
    - 3-я и 4-я строки поменяны местами,
    - 5-я и 6-я строки поменяны местами.
    Исходная матрица не изменяется.
    """
    return [
        matrix[1],  # Бывшая 2-я строка
        matrix[0],  # Бывшая 1-я строка
        matrix[3],  # Бывшая 4-я строка
        matrix[2],  # Бывшая 3-я строка
        matrix[5],  # Бывшая 6-я строка
        matrix[4]   # Бывшая 5-я строка
    ]

if __name__ == "__main__":
    # Генерация и вывод исходной матрицы
    original_matrix = create_matrix()
    print("Original Matrix:")
    print_matrix(original_matrix)

    # Получение новой матрицы с переставленными строками
    swapped_matrix = swap_rows(original_matrix)
    print("\nSwapped Matrix:")
    print_matrix(swapped_matrix)