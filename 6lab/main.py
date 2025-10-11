import func1
func1()
while True:
    command = input('''Выберите нужную команду из списка:
    1) Вставка элемента функцией пайтон
    2) Вставка алгоритмом
    3) Удалить элемент функцией пайтон
    4) Удалить элемент алгоритмом
    5) Нахождение К-го экстремума
    6) Наибольшая убывающая последовательность простых чисел
    7) Поменять местами наибольший отрицательный и последний нулевой
    0) Закончить выполнение команды
    Команда: ''')

    match command:
        
        case '1':
            listWithNumbers = list(map(int, input('Введите элементы массива через пробел: ').split()))
            index = int(input('Введите место подстановки: '))
            element = int(input('Введите новый элемент: '))
            listWithNumbers.insert(index, element)
            print(listWithNumbers)
            
        case '2':
            listWithNumbers = list(map(int, input('Введите элементы массива через пробел: ').split()))
            index = int(input('Введите место подстановки: '))
            element = int(input('Введите новый элемент: '))
            listWithNumbers.append(0)
            for i in range(len(listWithNumbers)):
                if i == index:
                    lastest = listWithNumbers[i]
                    listWithNumbers[i] = element
                elif i > index:
                    listWithNumbers[i], lastest = lastest, listWithNumbers[i]
            print(listWithNumbers)
            
        case '3':
            listWithNumbers = list(map(int, input('Введите элементы массива через пробел: ').split()))
            index = int(input('Введите индекс удаления: '))
            index = 4
            listWithNumbers.pop(index)
            print(listWithNumbers)
            
        case '4':
            listWithNumbers = list(map(int, input('Введите элементы массива через пробел: ').split()))
            index = int(input('Введите индекс удаления: '))
            
            for i in range(index, len(listWithNumbers) - 1):
                listWithNumbers[i] = listWithNumbers[i + 1]

            listWithNumbers = listWithNumbers[:-1]
            
            print(listWithNumbers)
            
        case '5':
            listWithNumbers = list(map(int, input('Введите элементы массива через пробел: ').split()))
            k = int(input('Введите К: '))
            numberOfFound = 0

            for i in range(1, len(listWithNumbers) - 1):
                leftNumber, number, rightNumber = listWithNumbers[i - 1 : i + 2]
                if (leftNumber < number and rightNumber < number) or \
                    (leftNumber > number and rightNumber > number):
                        numberOfFound += 1
                        
                        if numberOfFound == k:
                            print(number)
                            break
            else:
                print('Количество экстремумов меньше чем к')
            
        case '6':
            listWithNumbers = list(map(int, input('Введите элементы массива через пробел: ').split()))
        
            currentSequence = 0
            maxSequence = 0

            for index, value in enumerate(listWithNumbers):
                
                if value > 1:
                    numberIsPrime = True
                    for i in range(2, int(value**0.5)+1):
                        if value % i == 0:
                            numberIsPrime = False
                            break
                else:
                    numberIsPrime = False
                
                if numberIsPrime and currentSequence == 0:
                    currentSequence = 1
                elif numberIsPrime and value < listWithNumbers[index - 1]:
                    currentSequence += 1
                else:
                    maxSequence = max(currentSequence, maxSequence)
                    currentSequence = 0
                
            maxSequence = max(currentSequence, maxSequence)
            print(maxSequence)
            
        case '7':
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
                print(listWithNumbers)
            else:
                print('Значений в списке не хватает')
                
        case '0':
            break        
        case _:
            print('Неверный ввод команды')