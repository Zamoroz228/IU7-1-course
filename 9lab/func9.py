def input_matrix(text, input_type=float, squared=False):
    digits = '0123456789'
    
    if squared:
        row_number = column_number = int(input('Введите размер квадратной матрицы: '))
    else:
        row_number, column_number = map(int, input('Введите количество строчек и столбцов через пробел: ').split())

    if row_number <= 0 or column_number <= 0:
        print('Ошибка: Размер матрицы должен быть больше 0!')
        exit()
        
    matrix = []

    for i in range(row_number):
        dirty_list_input = input(f'Введите {i + 1} строчку: ').split()
        current_row = []
        
        if len(dirty_list_input) != column_number:
            print('Ошибка: Неверное количество данных в строке!')
            exit()
        
        if input_type == float:
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
            matrix.append(current_row)
            
        elif input_type == str:
            for char in dirty_list_input:
                if len(char) != 1:
                    print("Ошибка: Введен не символ, а строка!")
                    exit()
            matrix.append(dirty_list_input)
        
    s = f'{text}\n' + '-'*(9 * column_number + 1) + '\n'
    for i in matrix:
        for j in i:
            if input_type == float:
                s += f'|{j:^8.5g}'
            elif input_type == str:
                s += f'|{j:^8}'
        s += '|\n' + '-'*(9 * column_number + 1) + '\n'
    print(s)
    
    return matrix, row_number, column_number