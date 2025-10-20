'''
Поиск наиболее короткого элемента, не содержащего пробелов
'''

list_with_strings = []

print('Введите все строчки через enter - закончить ввод пустой строкой')

while True:
    current_string = input()
    
    if current_string == '':
        break
    
    list_with_strings.append(current_string)


min_string_len = float('inf')
min_string = None

for string in list_with_strings:
    
    if ' ' not in string and len(string) < min_string_len:
        min_string_len = len(string)
        min_string = string
        
if min_string is None:
    print('нет подходящего элемента')
else:
    print(f'Наименьшая длина: {min_string_len}\nСтрочка: {min_string}')  