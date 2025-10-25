'''
Найти столбец, имеющий наибольшее количество чисел, являющихся степенями 2.
'''
from math import log2
from func8 import input_matrix

matrix, size_of_matrix = input_matrix()

max_2degree_numbers = 0
column_index_with_max_degree2_numbers = None  

for index_column in range(size_of_matrix):
    amount_2degree_numbers = 0 
    for index_element in range(size_of_matrix):
        number = matrix[index_element][index_column]
        if number > 0 and log2(number) % 1 == 0:
            amount_2degree_numbers += 1
            
    if amount_2degree_numbers > max_2degree_numbers:
        max_2degree_numbers = amount_2degree_numbers
        column_index_with_max_degree2_numbers = index_column

if column_index_with_max_degree2_numbers is None:
    print('В матрице нет такого столбца')
else:
    print(f'Максимальное количество степеней двойки в одном столбце: {max_2degree_numbers}\n'
          f'Номер данного столбца: {column_index_with_max_degree2_numbers + 1}\n'
          f'Столбец: {[matrix[i][column_index_with_max_degree2_numbers] for i in range(size_of_matrix)]}')