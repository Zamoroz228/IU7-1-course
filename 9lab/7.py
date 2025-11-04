"""
Ввести трёхмерный массив (массив матриц размера X*Y*Z). Вывести срез
массива по большему измерению, индекс среза – середина размерности с
округлением в меньшую сторону.
"""

digits = '0123456789'
    
x_number, y_number, z_number = map(int, input('Введите размеры x y z через пробел: ').split())

if x_number <= 0 or y_number <= 0 or z_number <= 0:
    print('Ошибка: Размер матрицы должен быть больше 0!')
    exit()
    
massive_3D = []

for matrix_index in range(z_number):
    current_matrix = []
    for i in range(x_number):
        dirty_list_input = input(f'Введите {i + 1} строчку в матрице {matrix_index + 1}: ').split()
        current_row = []

        if len(dirty_list_input) != y_number:
            print('Ошибка: Неверное количество данных в строке!')
            exit()

        for number in dirty_list_input:
            is_negative = False
            is_float = False
            current_number = ''
            
            for char in number:
                if char == '-' and (not current_number or current_number[-1] == 'e'):
                    is_negative = not is_negative
                elif char == '.' and current_number and not is_float:
                    is_float = True
                    current_number += '.'
                elif char == '.' and is_float:
                    print('Ошибка: Неправильно введено ')
                    exit()
                elif char == 'e' or char == 'E':
                    current_number += 'e'
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
            
            current_row.append(float(current_number))
        current_matrix.append(current_row)
    massive_3D.append(current_matrix)
    
max_dimension = max(x_number, y_number, z_number)
slice_index = (max_dimension - 1) // 2

t = 0
for current_matrix in massive_3D:
    s = f'Срез по матрице с индексом {t}:\n' + '-'*(9 * y_number + 1) + '\n'
    for i in current_matrix:
        for j in i:
            s += f'|{j:^8.5g}'
        s += '|\n' + '-'*(9 * y_number + 1) + '\n'
    t += 1
    print(s)
    
print('\n','-'*100)

if max_dimension == z_number:
    s = f'Срез по матрице с индексом {slice_index}:\n' + '-'*(9 * y_number + 1) + '\n'
    for i in massive_3D[slice_index]:
        for j in i:
            s += f'|{j:^8.5g}'
        s += '|\n' + '-'*(9 * y_number + 1) + '\n'
    print(s)
    
elif max_dimension == x_number:
    s = f'Срез по строке с индексом {slice_index}:\n' + '-'*(9 * y_number + 1) + '\n'
    for matrix_index in range(z_number):
        for j in massive_3D[matrix_index][slice_index]:
            s += f'|{j:^8.5g}'
        s += '|\n' + '-'*(9 * y_number + 1) + '\n'
    print(s)
    
else:
    s = f'Срез по столбцу с индексом {slice_index}:\n' + '-'*(9 * x_number + 1) + '\n'
    for matrix_index in range(z_number):
        for row in massive_3D[matrix_index]:
            s += f'|{row[slice_index]:^8.5g}'
        s += '|\n' + '-'*(9 * x_number + 1) + '\n'
    print(s)