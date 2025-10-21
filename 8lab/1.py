'''
Найти строку, имеющую наименьшее количество чётных элементов.
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

max_even_numbers = 0
row_index_max_even = None  

for index, row in enumerate(matrix):
    amount_even_numbers = 0    
    for number in row:
        if number % 2 == 0:
            amount_even_numbers += 1
            
    if amount_even_numbers > max_even_numbers:
        max_even_numbers = amount_even_numbers
        row_index_max_even = index
        
if row_index_max_even is None:
    print('В матрице нет такой строчки')
else:
    print(f'Максимальное количество четных чисел в одной строчке: {max_even_numbers}\n'
          f'Номер данной строчки: {row_index_max_even + 1}')