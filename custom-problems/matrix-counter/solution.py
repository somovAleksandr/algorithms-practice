from random import randint


def create_matrix(cols=3, rows=4):
    """
    Создаёт матрицу размером rows x cols со случайными числами от -20 до 10.
    :param cols: количество столбцов
    :param rows: количество строк
    :return: двумерный список (матрица)
    """
    return [[randint(-20, 10) for _ in range(cols)] for _ in range(rows)]


def print_matrix(matrix):
    """
    Выводит матрицу в виде таблицы.
    :param matrix: двумерный список
    """
    for row in matrix:
        for num in row:
            print(f"{num:>4}", end="\t")  # выравнивание по правому краю
        print()


def count_negative_elements(matrix):
    """
    Считает количество отрицательных элементов в матрице.
    :param matrix: двумерный список
    :return: количество отрицательных чисел
    """
    count = 0
    for row in matrix:
        for num in row:
            if num < 0:
                count += 1
    return count


if __name__ == "__main__":
    matrix = create_matrix()
    print("Сгенерированная матрица:")
    print_matrix(matrix)
    negative_count = count_negative_elements(matrix)
    print(f"\nКоличество отрицательных элементов: {negative_count}")