'''
Выполнить транспонирование квадратной матрицы.
'''

from func8 import input_matrix

matrix, size_of_matrix = input_matrix()

for i in range(size_of_matrix):
    for j in range(i + 1, size_of_matrix):
        matrix[i][j], matrix[j][i] =\
        matrix[j][i], matrix[i][j]
        
print('Матрица после изменений: ')
[print(i) for i in matrix]