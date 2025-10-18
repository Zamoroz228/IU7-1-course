'''
К-го экстремум
'''
listWithNumbers = list(map(int, input('Введите элементы массива через пробел: ').split()))
k = int(input('Введите К: '))
if k < 0:
    print('К должен быть не отрицательный')
    
else:
    numberOfFound = 0

    for i in range(1, len(listWithNumbers) - 1):
        
        leftNumber, number, rightNumber = listWithNumbers[i - 1 : i + 2]
        
        if (leftNumber < number and rightNumber < number) or \
            (leftNumber > number and rightNumber > number):
                
                numberOfFound += 1
                
                if numberOfFound == k:
                    print('Найденное число:', number)
                    break
    else:
        print('Количество экстремумов меньше чем K')