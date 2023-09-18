
import random


def create_matrix(M):
    matrix = [[random.randint(1, 50) for _ in range(M)] for _ in range(M)]
    return matrix

def print_matrix(matrix):
    for row in matrix:
        formatted_row = "  ".join(f"{num:>3}" for num in row)
        print(f"[{formatted_row}]")


def sort_matrix(matrix):
    new_matrix = []

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    for col in range(num_cols):
        new_row = []
        for row in range(num_rows):
            new_row.append(matrix[row][col])
        new_matrix.append(new_row)

    matrix_with_sums = [(row, sum(row)) for row in new_matrix]

    M = len(new_matrix)
    for i in range(M):
        for j in range(0, M - i - 1):
            if matrix_with_sums[j][1] > matrix_with_sums[j + 1][1]:
                matrix_with_sums[j], matrix_with_sums[j + 1] = matrix_with_sums[j + 1], matrix_with_sums[j]

    sorted_matrix = [row for row, _ in matrix_with_sums]

    n = len(sorted_matrix)

    for i, row in enumerate(sorted_matrix):
        sorted_asc = False
        sorted_desc = False

        if i % 2 == 0:
            while not sorted_asc:
                sorted_asc = True
                for j in range(n - 1):
                    for k in range(n - 1 - j):
                        if sorted_matrix[i][k] < sorted_matrix[i][k + 1]:
                            sorted_matrix[i][k], sorted_matrix[i][k + 1] = sorted_matrix[i][k + 1], sorted_matrix[i][k]
                            sorted_asc = False
        else:
            while not sorted_desc:
                sorted_desc = True
                for j in range(n - 1):
                    for k in range(n - 1 - j):
                        if sorted_matrix[i][k] > sorted_matrix[i][k + 1]:
                            sorted_matrix[i][k], sorted_matrix[i][k + 1] = sorted_matrix[i][k + 1], sorted_matrix[i][k]
                            sorted_desc = False

    row_sums = [sum(row) for row in sorted_matrix]

    restore_matrix = []
    num_rows1 = len(sorted_matrix)
    num_cols1 = len(matrix[0])

    for cols in range(num_cols1):
        new_row1 = []
        for rows in range(num_rows1):
            new_row1.append(sorted_matrix[rows][cols])
        restore_matrix.append(new_row1)
    restore_matrix.append(row_sums)
    return restore_matrix


M = int(input("Введите размер матрицы (M > 5): "))
if M <= 5:
    print("Размер матрицы должен быть больше 5.")
else:
    matrix = create_matrix(M)
    print("Исходная матрица:")
    print_matrix(matrix)
    sorted_matrix = sort_matrix(matrix)
    print("\nОтсортированная матрица:")
    print_matrix(sorted_matrix)

