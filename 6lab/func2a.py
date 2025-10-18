'''
Удаление элемента из массива
'''
listWithNumbers = list(map(int, input('Введите элементы массива через пробел: ').split()))
index = int(input('Введите индекс удаления: '))
if index >= len(listWithNumbers) or index < 0:
    print('Неверный индекс')

else:
    listWithNumbers.pop(index)

    print('Массив после изменений:', listWithNumbers)