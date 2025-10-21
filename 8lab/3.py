'''
Найти столбец, имеющий наибольшее количество чисел, являющихся степенями 2.
'''
from math import log2

digits = '0123456789'

size_of_matrix = int(input('Введите размер квадратной матрицы: '))
if size_of_matrix <= 0:
    print('Ошибка: Размер матрицы должен быть больше 0!')
    exit()
    
matrix = []

for i in range(size_of_matrix):
    dirty_list_input = input(f'Введите {i + 1} строчку: ').split()
    current_row = []
    
    if len(dirty_list_input) != size_of_matrix:
        print('Ошибка: Неверное количество данных в строке!')
        exit()
    
    for number in dirty_list_input:
        is_negative = False
        current_number = ''
        
        for char in number:
            if char == '-' and not current_number:
                is_negative = not is_negative
            elif char in digits:
                current_number += char
            else:
                print('Ошибка: Введен символ отличный от цифр!')
                exit()
        
        if not current_number:
            print('Ошибка: Число полностью состоит из минусов!')
            exit()
        
        if is_negative:
            current_number = '-' + current_number
        
        current_row.append(int(current_number))
    
    matrix.append(current_row)

list_with_columns = list(zip(*matrix))

max_2degree_numbers = 0
column_index_with_max_degree2_numbers = None  

for index, column in enumerate(list_with_columns):
    amount_2degree_numbers = 0    
    for number in column:
        if number > 0 and log2(number) % 1 == 0:
            amount_2degree_numbers += 1
            
    if amount_2degree_numbers > max_2degree_numbers:
        max_2degree_numbers = amount_2degree_numbers
        column_index_with_max_degree2_numbers = index

if column_index_with_max_degree2_numbers is None:
    print('В матрице нет такого столбца')
else:
    print(f'Максимальное количество степеней двойки в одном столбце: {max_2degree_numbers}\n'
          f'Номер данного столбца: {column_index_with_max_degree2_numbers + 1}\n'
          f'Столбец: {list_with_columns[column_index_with_max_degree2_numbers]}')