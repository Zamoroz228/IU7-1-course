"""
Дана матрица символов. Преобразовать её следующим образом: заменить все
согласные латинские букв на заглавные, а все гласные латинские буквы на
строчные. Вывести матрицу до преобразования и после.
"""

from func9 import input_matrix

matrix, row_number, column_number = input_matrix('Изначальная матрица:', input_type=str) # type: ignore

consonants_chars = 'bcdfghjklmnpqrstvwxyz'
vowels_chars = 'AEIOU'

for i in range(row_number):
    for j in range(column_number):
        if matrix[i][j] in consonants_chars:
            matrix[i][j] = chr(ord(matrix[i][j]) - 32)
            
        if matrix[i][j] in vowels_chars:
            matrix[i][j] = chr(ord(matrix[i][j]) + 32)
            
s = 'Матрица после изменений:\n' + '-'*(9 * column_number + 1) + '\n'
for i in matrix:
    for j in i:
        s += f'|{j:^8}'
    s += '|\n' + '-'*(9 * column_number + 1) + '\n'
print(s)