'''
Даны две матрицы A и B, в которых количество столбцов одинаково.
Подсчитать для каждого столбца матрицы А количество элементов, больших
среднего арифметического элементов соответствующего столбца матрицы В.
Вывести полученные значения. Затем преобразовать матрицу В путем
умножения всех элементов столбца матрицы на посчитанное для этого столбца
значение, если оно ненулевое. Вывести преобразованную матрицу в виде
матрицы.
'''

from func9 import input_matrix

print('Введ матрицы A:')
a_matrix, a_row_number, a_column_number = input_matrix('Исходная матрица A:')

print('Введ матрицы B:')
b_matrix, b_row_number, b_column_number = input_matrix('Исходная матрица B:')

if a_column_number != b_column_number:
    print('Ошибка: Количество столбцов матрицы A и B не совпадает!')
    exit()
    
for column_index in range(a_column_number):
    
    average_value = 0
    for row_index in range(b_row_number):
        average_value += b_matrix[row_index][column_index]
    average_value /= b_row_number
    
    amount_large_a_element = 0
    for row_index in range(a_row_number):
        amount_large_a_element += 1 if a_matrix[row_index][column_index] > average_value else 0
        
    print(f'Количество значений в столбце {column_index + 1} матрицы A больших чем среднее столбца B: ', amount_large_a_element)
    
    if amount_large_a_element:
        for row_index in range(b_row_number):
            b_matrix[row_index][column_index] *= amount_large_a_element
    
s = 'Матрица B после изменений:\n' + '-'*(9 * b_column_number + 1) + '\n'
for i in b_matrix:
    for j in i:
        s += f'|{j:^8.5g}'
    s += '|\n' + '-' * (9 * b_column_number + 1) + '\n'
print(s)