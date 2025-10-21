'''
Переставить местами строки с наибольшим и наименьшим количеством
отрицательных элементов.
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