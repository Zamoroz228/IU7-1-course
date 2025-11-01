'''
Задана матрица D и массив I, содержащий номера строк, для которых
необходимо определить максимальный элемент. Значения максимальных
элементов запомнить в массиве R. Определить среднее арифметическое
вычисленных максимальных значений. Напечатать матрицу D, массивы I и R,
среднее арифметическое значение.
'''

from func9 import input_matrix

d_matrix, row_number, column_number = input_matrix('Матрица D:')
i_massive = list(map(int, input('Введите массив I: ').split()))
r_massive = []

average_value = 0
for row_index in i_massive:
    row_index -= 1
    if row_index < 0 or row_index >= row_number:
        print('Ошибка: Номера строк в массиве не соотвествуют номерам строк в матрице!')
        exit()
    
    max_element = d_matrix[row_index][0]
    for column_index in range(column_number):
        max_element = max(max_element, d_matrix[row_index][column_index])
    
    average_value += max_element
    r_massive.append(max_element)

average_value /= len(i_massive)

print(f"Массив I: {'|'.join([f'{i:^6}' for i in i_massive])}\n"
      f"Массив R: {'|'.join([f'{r:^6.5g}' for r in r_massive])}\n"
      f"Среднее значение: {average_value}")