'''
Переставить местами столбцы с максимальной и минимальной суммой
элементов.
'''

from func8 import input_matrix

matrix, size_of_matrix = input_matrix()

max_column_sum_numbers = float('-inf')
index_max_sum_numbers = None  

min_column_sum_numbers = float('inf')
index_min_sum_numbers = None  

for index_column in range(size_of_matrix):
    current_sum = 0
    for index_element in range(size_of_matrix):
        number = matrix[index_element][index_column]
        current_sum += number
    
    if current_sum > max_column_sum_numbers:
        max_column_sum_numbers = current_sum
        index_max_sum_numbers = index_column
    
    if current_sum < min_column_sum_numbers:
        min_column_sum_numbers = current_sum
        index_min_sum_numbers = index_column

for index_element in range(size_of_matrix):
    matrix[index_element][index_min_sum_numbers], matrix[index_element][index_max_sum_numbers] =\
    matrix[index_element][index_max_sum_numbers], matrix[index_element][index_min_sum_numbers]
    
if index_max_sum_numbers is None or index_max_sum_numbers is None:
    print('В матрице недостаточно данных')
else:
    print('Матрица после изменений:')
    [print(i) for i in matrix]