'''
Переставить местами строки с наибольшим и наименьшим количеством
отрицательных элементов.
'''
from func8 import input_matrix

matrix, size_of_matrix = input_matrix()


max_amount_negative_numbers = 0
row_index_max_negative = None

min_amount_negative_numbers = size_of_matrix
row_index_min_negative = None

for index, row in enumerate(matrix):
    amount_negative_numbers = 0    
    for number in row:
        if number < 0:
            amount_negative_numbers += 1
            
    if amount_negative_numbers > max_amount_negative_numbers:
        max_amount_negative_numbers = amount_negative_numbers
        row_index_max_negative = index
    
    if amount_negative_numbers < min_amount_negative_numbers:
        min_amount_negative_numbers = amount_negative_numbers
        row_index_min_negative = index
        
if row_index_max_negative is None or row_index_min_negative is None:
    print('В матрице недостаточно данных')
else:
    matrix[row_index_min_negative], matrix[row_index_max_negative] =\
    matrix[row_index_max_negative], matrix[row_index_min_negative] 
    
    print('Матрица после изменений:')
    [print(i) for i in matrix]