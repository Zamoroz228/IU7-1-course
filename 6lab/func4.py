listWithNumbers = list(map(int, input('Введите элементы массива через пробел: ').split()))
index = int(input('Введите индекс удаления: '))

for i in range(index, len(listWithNumbers) - 1):
    listWithNumbers[i] = listWithNumbers[i + 1]

listWithNumbers = listWithNumbers[:-1]

print('Массив после изменений:', listWithNumbers)
