'''
Найти максимальное значение в квадратной матрице над главной диагональю и
минимальное - под побочной диагональю.
'''

from func8 import input_matrix

matrix, size_of_matrix = input_matrix()

max_above_main_diagonal = float('-inf')
min_below_secondary_diagonal = float('inf')
    
for i in range(size_of_matrix):
    for j in range(size_of_matrix):
        if i < j:
            if matrix[i][j] > max_above_main_diagonal:
                max_above_main_diagonal = matrix[i][j]
            
        if i + j > size_of_matrix - 1:
            if matrix[i][j] < min_below_secondary_diagonal:
                min_below_secondary_diagonal = matrix[i][j]
            
if max_above_main_diagonal != float('-inf') and min_below_secondary_diagonal != float('inf'):
    print(f'Максимальный элемент над главной диагональю: {max_above_main_diagonal}\n'
          f'Минимальный элемент под побочной диагональю: {min_below_secondary_diagonal}')
else:
    print('Недостоточно данных')