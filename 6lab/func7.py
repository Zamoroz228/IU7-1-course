listWithNumbers = list(map(int, input('Введите элементы массива через пробел: ').split()))

lastZeroPosition = -1

maxNegativeValue = float('-inf')
maxNegativePosition = -1

for index, value in enumerate(listWithNumbers):
    
    if value == 0:
        lastZeroPosition = index
    
    if maxNegativeValue < value < 0:
        maxNegativeValue = value
        maxNegativePosition = index

if maxNegativePosition != -1 and lastZeroPosition != -1:
    listWithNumbers[maxNegativePosition], listWithNumbers[lastZeroPosition] =\
    listWithNumbers[lastZeroPosition], listWithNumbers[maxNegativePosition]
    print('Массив после изменений:', listWithNumbers)
    
else:
    print('Значений в списке не хватает')
    