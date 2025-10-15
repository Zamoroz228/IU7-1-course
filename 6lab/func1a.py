'''
Добавление элемента в массив
'''
listWithNumbers = list(map(int, input('Введите элементы массива через пробел: ').split()))
index = int(input('Введите индекс подстановки: '))
element = int(input('Введите новый элемент: '))
listWithNumbers.insert(index, element)
print('Массив после изменений:', listWithNumbers)