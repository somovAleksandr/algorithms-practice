def print_matrix(matrix):
    """
    Выводит двумерную матрицу в удобочитаемом табличном виде.
    
    Аргументы:
        matrix (list of lists): Двумерный список (матрица) чисел.
    
    Пример вывода:
        1       2       3       4
        5       6       7       8
        9       10      11      12
    """
    for row in matrix:
        for element in row:
            print(element, end='\t\t')  # Два таба между числами
        print()  # Переход на новую строку после каждой строки матрицы


def print_matrix_squared(matrix):
    """
    Выводит матрицу, в которой каждый элемент — квадрат исходного.
    
    Аргументы:
        matrix (list of lists): Исходная матрица чисел.
    
    Пример (для элемента 3 → 3² = 9):
        1       4       9       16
        25      36      49      64
        81      100     121     144
    """
    for row in matrix:
        for element in row:
            print(element ** 2, end='\t\t')  # Вывод квадрата числа
        print()  # Переход на новую строку


if __name__ == "__main__":
    matrix = [
        [1,  2,  3,  4],
        [5,  6,  7,  8],
        [9, 10, 11, 12]
    ]

    print(" Исходная матрица ")
    print_matrix(matrix)

    print("\n Матрица квадратов ")
    print_matrix_squared(matrix)