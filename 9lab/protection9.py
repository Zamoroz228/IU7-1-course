'''

'''


n, m = map(int, input('Введите размерность матрицы: ').split())

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

s = list(map(int, input().split()))
list_with_coord = [False] * 3

for i in range(n):
    for j in range(m):
        if matrix[i][j] == s[0]:
            list_with_coord[0] = (i, j) # type: ignore
        elif matrix[i][j] == s[1]:
            list_with_coord[1] = (i, j) # type: ignore
        elif matrix[i][j] == s[2]:
            list_with_coord[2] = (i, j) # type: ignore

if all(list_with_coord):
    i0, j0 = list_with_coord[0] # type: ignore
    i1, j1 = list_with_coord[1] # type: ignore
    i2, j2 = list_with_coord[2] # type: ignore
    if (i0 - j0 == i1 - j1 == i2 - j2):
        print('Все элементы лежат на нормальной диагонали')
    elif (i0 + j0 == i1 + j1 == i2 + j2):
        print('Все элементы лежат на другой диагонали')
    else:
        print('Все элементы лежат рандомно')
else:
    print('Не все значения')