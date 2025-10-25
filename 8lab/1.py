'''
Найти строку, имеющую наименьшее количество чётных элементов.
'''
from func8 import input_matrix

matrix, size_of_matrix = input_matrix()

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