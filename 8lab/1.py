'''
Найти строку, имеющую наименьшее количество чётных элементов.
'''
from func8 import input_matrix

matrix, row_number, column_number = input_matrix()

min_even_numbers = row_number + 1
row_index_min_even = None  

for index, row in enumerate(matrix):
    amount_even_numbers = 0    
    for number in row:
        if number % 2 == 0:
            amount_even_numbers += 1
            
    if amount_even_numbers < min_even_numbers:
        min_even_numbers = amount_even_numbers
        row_index_min_even = index
        
if row_index_min_even is None:
    print('В матрице нет такой строчки\n')
else:
    print(f'Наименьшее количество четных чисел в одной строчке: {min_even_numbers}\n'
          f'Номер данной строчки: {row_index_min_even + 1}\n')