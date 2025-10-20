'''
Замена всех цифр на пробелы
'''
digits = '0123456789'

list_with_strings = []

print('Введите все строчки через enter - закончить ввод пустой строки')

while True:
    current_string = input()
    
    if current_string == '':
        break
    
    list_with_strings.append(current_string)

for i in range(len(list_with_strings)):
    # for digit in digits:
    #     list_with_strings[i] = list_with_strings[i].replace(digit, ' ')
    
    new_s = ''
    for char_indx in range(len(list_with_strings[i])):
        if list_with_strings[i][char_indx] in digits:
            new_s += ' '
        else:
            new_s += list_with_strings[i][char_indx]
    list_with_strings[i] = new_s
            
print('-'*44)
[print(i) for i in list_with_strings]