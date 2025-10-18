'''
Замена максимального отрицательного и последнего нуля
'''
listWithNumbers = list(map(int, input('Введите элементы массива через пробел: ').split()))

maxNegativeValue = float('-inf')
maxNegativePosition = None

for index, value in enumerate(listWithNumbers):
    
    if value == 0:
        lastZeroPosition = index
    
    if maxNegativeValue < value < 0:
        maxNegativeValue = value
        maxNegativePosition = index

if not maxNegativePosition is None and not lastZeroPosition is None:
    listWithNumbers[maxNegativePosition], listWithNumbers[lastZeroPosition] =\
    listWithNumbers[lastZeroPosition], listWithNumbers[maxNegativePosition]
    print('Массив после изменений:', listWithNumbers)
    
else:
    print('Значений в списке не хватает')