'''
Переставить местами столбцы с максимальной и минимальной суммой
элементов.
'''

from func8 import input_matrix

matrix, row_number, column_number = input_matrix()

max_column_sum_numbers = float('-inf')
index_max_sum_numbers = None  

min_column_sum_numbers = float('inf')
index_min_sum_numbers = None  

for index_column in range(column_number):
    current_sum = 0
    for index_element in range(row_number):
        number = matrix[index_element][index_column]
        current_sum += number
    
    if current_sum > max_column_sum_numbers:
        max_column_sum_numbers = current_sum
        index_max_sum_numbers = index_column
    
    if current_sum < min_column_sum_numbers:
        min_column_sum_numbers = current_sum
        index_min_sum_numbers = index_column

for index_element in range(row_number):
    matrix[index_element][index_min_sum_numbers], matrix[index_element][index_max_sum_numbers] =\
    matrix[index_element][index_max_sum_numbers], matrix[index_element][index_min_sum_numbers]
    
if index_max_sum_numbers is None or index_max_sum_numbers is None:
    print('В матрице недостаточно данных\n')
else:
    s = 'Матрица после изменений:\n' + '-'*(9 * column_number + 1) + '\n'
    for i in matrix:
        for j in i:
            s += f'|{j:^8.5g}'
        s += '|\n' + '-'*(9 * column_number + 1) + '\n'
    print(s)