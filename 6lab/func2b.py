'''
Алгоритмическое удаление элемента из массива
'''
listWithNumbers = list(map(int, input('Введите элементы массива через пробел: ').split()))
index = int(input('Введите индекс удаления: '))
if index >= len(listWithNumbers) or index < 0:
    print('Неверный индекс')

else:
    for i in range(index + 1, len(listWithNumbers)):
        listWithNumbers[i - 1] = listWithNumbers[i]

    listWithNumbers = listWithNumbers[:-1]

    print('Массив после изменений:', listWithNumbers)