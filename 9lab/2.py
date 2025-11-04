'''
Повернуть квадратную целочисленную матрицу на 90 градусов по часовой
стрелке, затем на 90 градусов против часовой стрелки. Вывести исходную,
промежуточную и итоговую матрицы. Дополнительных матриц и массивов не
вводить. Транспонирование не применять.
'''

from func9 import input_matrix

matrix, size_of_matrix, _ = input_matrix('Исходная матрица: ', squared=True)
n = size_of_matrix

for i in range(n // 2):
    for j in range(i, n - i - 1):
        temp = matrix[i][j]
        matrix[i][j] = matrix[n - 1 - j][i]
        matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
        matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
        matrix[j][n - 1 - i] = temp

s = 'Матрица после поворота направо:\n' + '-'*(9 * size_of_matrix + 1) + '\n'
for i in matrix:
    for j in i:
        s += f'|{j:^8.5g}'
    s += '|\n' + '-'*(9 * size_of_matrix + 1) + '\n'
print(s)

for i in range(n // 2):
    for j in range(i, n - i - 1):
        temp = matrix[i][j]
        matrix[i][j] = matrix[j][n - 1 - i]
        matrix[j][n - 1 - i] = matrix[n - 1 - i][n - 1 - j]
        matrix[n - 1 - i][n - 1 - j] = matrix[n - 1 - j][i]
        matrix[n - 1 - j][i] = temp

s = 'Матрица после поворота налево:\n' + '-'*(9 * size_of_matrix + 1) + '\n'
for i in matrix:
    for j in i:
        s += f'|{j:^8.5g}'
    s += '|\n' + '-'*(9 * size_of_matrix + 1) + '\n'
print(s)