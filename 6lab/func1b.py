'''
Алгоретмическое добавление элемента в массив
'''
listWithNumbers = list(map(int, input('Введите элементы массива через пробел: ').split()))
index = int(input('Введите индекс подстановки: '))
element = int(input('Введите новый элемент: '))

listWithNumbers.append(None) # type: ignore

for i in range(len(listWithNumbers) - 1, index, -1):
    listWithNumbers[i] = listWithNumbers[i - 1]
    
listWithNumbers[index] = element
print('Массив после изменений:', listWithNumbers)