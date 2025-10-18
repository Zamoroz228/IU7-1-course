'''вводим последовательность и в ней замена среднее арифмитическое четных, вместо 3 максимального элемента'''

listWithNumbers = list(map(int, input().split()))
avg = 0
avgcount = 0

firstMax = secondMax = thirdMax = float('-inf')
firstMaxIndex = secondMaxIndex = thirdMaxIndex = None

for i, value in enumerate(listWithNumbers):
    if i % 2 == 0:
        avg += value
        avgcount += 1
    
    if firstMax <= value:
        thirdMax = secondMax
        secondMax = firstMax
        firstMax = value
        
        thirdMaxIndex = secondMaxIndex
        secondMaxIndex = firstMaxIndex 
        firstMaxIndex = i
        
    elif secondMax <= value:
        thirdMax = secondMax
        secondMax = value
        
        thirdMaxIndex = secondMaxIndex
        secondMaxIndex = i
    
    elif thirdMax <= value:
        thirdMax = value
        
        thirdMaxIndex = i
        
if thirdMaxIndex is None:
    print('не хватает элементов')
else:
    listWithNumbers[thirdMaxIndex] = avg / avgcount # type: ignore
    print(listWithNumbers)