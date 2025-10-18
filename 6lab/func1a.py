'''
Добавление элемента в массив
'''
listWithNumbers = list(map(int, input('Введите элементы массива через пробел: ').split()))
index = int(input('Введите индекс подстановки: '))
if index > len(listWithNumbers) or index < 0:
    print('Неверный индекс')

else:
    element = int(input('Введите новый элемент: '))
    listWithNumbers.insert(index, element)
    print('Массив после изменений:', listWithNumbers)