'''
Найти столбец, имеющий наибольшее количество чисел, являющихся степенями 2.
'''
from func8 import input_matrix

matrix, row_number, column_number = input_matrix()

max_2degree_numbers = 0
column_index_with_max_degree2_numbers = None  

f = 1.1

for index_column in range(column_number):
    amount_2degree_numbers = 0 
    for index_element in range(row_number):
        number = matrix[index_element][index_column]
        if number > 0 and number % 1 == 0 and (int(number) & int(number - 1)) == 0:
            amount_2degree_numbers += 1
            
    if amount_2degree_numbers > max_2degree_numbers:
        max_2degree_numbers = amount_2degree_numbers
        column_index_with_max_degree2_numbers = index_column

if column_index_with_max_degree2_numbers is None:
    print('В матрице нет такого столбца\n')
else:
    print(f'Максимальное количество степеней двойки в одном столбце: {max_2degree_numbers}\n'
          f'Номер данного столбца: {column_index_with_max_degree2_numbers + 1}\n'
          f'Столбец: {' '.join([f'{matrix[i][column_index_with_max_degree2_numbers]:.5g}' for i in range(row_number)])}\n')