'''
Максимальная убывающая последовательность простых чисел
'''
listWithNumbers = list(map(int, input('Введите элементы массива через пробел: ').split()))

currentSequenceLen = 0
currentSequence = [] 

maxSequenceLen = 0
maxSequence = []

for index, value in enumerate(listWithNumbers):
    
    if value > 1:
        numberIsPrime = True
        for i in range(2, int(value**0.5)+1):
            if value % i == 0:
                numberIsPrime = False
                break
    else:
        numberIsPrime = False
    
    if numberIsPrime and currentSequenceLen == 0:
        currentSequenceLen = 1
        currentSequence = [value]
        
    elif numberIsPrime and value < listWithNumbers[index - 1]:
        currentSequenceLen += 1
        currentSequence.append(value)
        
    else:
        if currentSequenceLen > maxSequenceLen:
            maxSequenceLen = currentSequenceLen
            maxSequence = currentSequence

        currentSequenceLen = 0
    
if currentSequenceLen > maxSequenceLen:
            maxSequenceLen = currentSequenceLen
            maxSequence = currentSequence

print('Максмальная длинна такой последовательности: ', maxSequenceLen)
print('Максимальная последовательность:', maxSequence)