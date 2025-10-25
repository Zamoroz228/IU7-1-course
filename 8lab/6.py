'''
Выполнить транспонирование квадратной матрицы.
'''

from func8 import input_matrix

matrix, size_of_matrix, _ = input_matrix(squared=True)


for i in range(size_of_matrix):
    for j in range(i + 1, size_of_matrix):
        matrix[i][j], matrix[j][i] =\
        matrix[j][i], matrix[i][j]
        
s = 'Транспонированная матрица:\n' + '-'*(9 * size_of_matrix + 1) + '\n'
for i in matrix:
    for j in i:
        s += f'|{j:^8.5g}'
    s += '|\n' + '-'*(9 * size_of_matrix + 1) + '\n'
print(s)