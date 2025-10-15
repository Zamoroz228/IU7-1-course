'''
Удаление элемента из массива
'''
listWithNumbers = list(map(int, input('Введите элементы массива через пробел: ').split()))
index = int(input('Введите индекс удаления: '))

listWithNumbers.pop(index)

print('Массив после изменений:', listWithNumbers)
