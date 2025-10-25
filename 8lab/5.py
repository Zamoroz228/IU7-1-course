'''
Найти максимальное значение в квадратной матрице над главной диагональю и
минимальное - под побочной диагональю.
'''
from func8 import input_matrix

size_of_matrix = int(input('Введите размер квадратной матрицы: '))
matrix = [[0.0]*size_of_matrix for _ in range(size_of_matrix)]

for i in range(size_of_matrix):
    for j in range(size_of_matrix):
        matrix[i][j] = float(input(f'Введите значение строки {i + 1} и столбца {j + 1}: '))

s = 'Матрица до изменений:\n' + '-'*(9 * size_of_matrix + 1) + '\n'
for i in matrix:
    for j in i:
        s += f'|{j:^8.5g}'
    s += '|\n' + '-'*(9 * size_of_matrix + 1) + '\n'
print(s)

max_above_main_diagonal = float('-inf')
min_below_secondary_diagonal = float('inf')
    
for i in range(size_of_matrix):
    for j in range(i + 1, size_of_matrix):
        if matrix[i][j] > max_above_main_diagonal:
            max_above_main_diagonal = matrix[i][j]
            
for i in range(size_of_matrix):
    for j in range(size_of_matrix - i, size_of_matrix):
        if matrix[i][j] < min_below_secondary_diagonal:
            min_below_secondary_diagonal = matrix[i][j]

if max_above_main_diagonal != float('-inf') and min_below_secondary_diagonal != float('inf'):
    print(f'Максимальный элемент над главной диагональю: {max_above_main_diagonal:.5g}\n'
          f'Минимальный элемент под побочной диагональю: {min_below_secondary_diagonal:.5g}\n')
else:
    print('Недостоточно данных\n')