from random import randint

def create_matrix():
    """Создаёт матрицу 4x3 со случайными числами от 0 до 4."""
    return [[randint(0, 4) for _ in range(3)] for _ in range(4)]

def print_matrix(matrix):
    """Выводит матрицу в виде таблицы."""
    for row in matrix:
        for num in row:
            print(f"{num:2}", end="\t")
        print()

def prod_positive_nums(matrix):
    """Возвращает произведение всех положительных (ненулевых) элементов матрицы."""
    result = 1
    for lst in matrix:
        for num in lst:
            if num > 0:
                result *= num
    return result

# Основная программа
if __name__ == "__main__":
    matrix = create_matrix()
    print("Сгенерированная матрица:")
    print_matrix(matrix)
    res = prod_positive_nums(matrix)
    print("Произведение ненулевых элементов:", res)