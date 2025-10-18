'''
Замена всех цифр на пробелы
'''
from string import digits

list_with_strings = []

print('Введите все строчки через enter - закончить ввод 0')

current_string = input()

while current_string != '0':
    list_with_strings.append(current_string)

    current_string = input()
    


for i in range(len(list_with_strings)):
    for digit in digits:
        list_with_strings[i] = list_with_strings[i].replace(digit, ' ')

[print(i) for i in list_with_strings]