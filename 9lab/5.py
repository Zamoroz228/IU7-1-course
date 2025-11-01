"""
Даны 2 матрицы А и В. Получить матрицу С, равную произведению матриц А и
В. Вывести все матрицы в виде матриц.
"""

from func9 import input_matrix

print('Ввод матрицы A:')
a_matrix, a_row_number, a_column_number = input_matrix('Матрица A:')

print('Ввод матрицы B:')
b_matrix, b_row_number, b_column_number = input_matrix('Матрица B:')

if a_column_number != b_row_number:
    print('Ошибка: Количество столбцов A и строк B не совпадают!')
    exit()

c_matrix = [[0] * b_column_number for _ in range(a_row_number)]

for i in range(a_row_number):
    for j in range(b_column_number):
        for k in range(a_column_number):
            c_matrix[i][j] += a_matrix[i][k] * b_matrix[k][j]

s = 'Матрица C результат умножения A и B:\n' + '-'*(9 * b_column_number + 1) + '\n'
for i in c_matrix:
    for j in i:
        s += f'|{j:^8.5g}'
    s += '|\n' + '-'*(9 * b_column_number + 1) + '\n'
print(s)