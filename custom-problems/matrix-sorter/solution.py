from copy import deepcopy

def print_matrix(matrix):
    for row in matrix:
        for num in row:
            print(num, end="\t")
        print()

matrix = [[2, 5, 8], [5, 8, 2], [8, 7, 1], [0, 7, 1], [9, 11, 6]]

def sort_matrix_by_pattern(matrix):
    matrix_copy = deepcopy(matrix)
    
    for i in range(len(matrix_copy)):
        if i % 2 == 0:  
            matrix_copy[i].sort(reverse=True)
        else: 
            matrix_copy[i].sort()
    
    return matrix_copy

result_matrix = sort_matrix_by_pattern(matrix)

print("Исходная матрица:")
print_matrix(matrix)
print("\nПреобразованная матрица:")
print_matrix(result_matrix)