from random import randint


def get_list_size():
    while True:
        input_message = input("Введите размерность массива: ")
        try:
            size = int(input_message)
            if size <= 0:
                print("Нужно ввести число больше НУЛЯ...")
                continue
            return size
        except ValueError:
            print("Ошибка! Некорректный ввод. Попробуйте еще раз.")


def create_matrix(size):
    return [[randint(1, 100) for _ in range(size)] for _ in range(size)]


def print_matrix(matrix):
    print("Матрица:")
    for row in matrix:
        for num in row:
            print(num, end="\t\t")
        print()  # новая строка после строки матрицы


def get_min_diagonal_element(matrix):
    if len(matrix) == 0:
        raise ValueError("Матрица пустая — нет диагонали.")
    
    # Собираем элементы главной диагонали: matrix[0][0], matrix[1][1], ...
    diagonal = []
    for i in range(len(matrix)):
        diagonal.append(matrix[i][i])
    return min(diagonal)


# === Основная программа ===
size = get_list_size()
matrix = create_matrix(size)
print_matrix(matrix)

min_diagonal = get_min_diagonal_element(matrix)
print(f"Минимальный элемент на главной диагонали: {min_diagonal}")