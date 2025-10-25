'''
Переставить местами столбцы с максимальной и минимальной суммой
элементов.
'''

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