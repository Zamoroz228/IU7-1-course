'''Даны два одномерных целочисленных массива A и B. Сформировать матрицу
M, такую что
Mij = Ai * Bj
Определить количество полных квадратов в каждой строке матрицы.Записать
значения в массив S. Напечатать матрицу M в виде матрицы и рядом столбец
S.
'''

a = list(map(int, input('Введите массив A: ').split()))
b = list(map(int, input('Введите массив B: ').split()))

matrix = [[0]*len(b) for _ in range(len(a))]
s = []

for i in range(len(a)):
    amount_squares = 0
    for j in range(len(b)):
        value = a[i] * b[j]
        if value > 0 and int(value ** 0.5) ** 2 == value:
            amount_squares += 1
            
        matrix[i][j] = value

    s.append(amount_squares)
        
string = 'Новая матрица и столбец S:\n' + '-'*(9 * (len(b) + 1) + 1) + '\n'
for i in range(len(matrix)):
    for j in matrix[i]:
        string += f'|{j:^8}'
    string += f'|{s[i]:^8}'
    string += '|\n' + '-'*(9 * (len(b) + 1) + 1) + '\n'
print(string)