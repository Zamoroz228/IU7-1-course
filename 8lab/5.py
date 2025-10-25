'''
Найти максимальное значение в квадратной матрице над главной диагональю и
минимальное - под побочной диагональю.
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

max_above_main_diagonal = float('-inf')
min_below_secondary_diagonal = float('inf')
    
for i in range(size_of_matrix):
    for j in range(size_of_matrix):
        if i < j:
            max_above_main_diagonal = max(max_above_main_diagonal, matrix[i][j])
            
        if i + j > size_of_matrix - 1:
            min_below_secondary_diagonal = min(min_below_secondary_diagonal, matrix[i][j])
            
if max_above_main_diagonal != float('-inf') and min_below_secondary_diagonal != float('inf'):
    print(f'Максимальный элемент над главной диагональю: {max_above_main_diagonal}\n'
          f'Минимальный элемент под побочной диагональю: {min_below_secondary_diagonal}')
else:
    print('Недостоточно данных')