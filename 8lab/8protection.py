'''макс элемент и его транспонировать'''

from re import L


size_of_matrix = int(input('size matrix: '))

matrix = []

for i in range(size_of_matrix):
    matrix.append(list(map(int, input(f'row {i + 1}: ').split())))

max_element = matrix[0][0]
max_r = 0
max_c = 0

for i in range(size_of_matrix):
    for j in range(size_of_matrix):
        if matrix[i][j] > max_element:
            max_element = matrix[i][j]
            max_r = i
            max_c = j

new_matrix = []
for i in matrix:
    new_matrix.append(i.copy())

for i in range(size_of_matrix):
    new_matrix[max_r][i], new_matrix[i][max_c] = matrix[i][max_c], matrix[max_r][i]
    
print('-'*10)
[print(*i) for i in new_matrix]