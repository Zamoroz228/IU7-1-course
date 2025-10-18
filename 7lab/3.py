'''
Поиск наиболее короткого элемента, не содержащего пробелов
'''

list_with_strings = []

print('Введите все строчки через enter - закончить ввод 0')

current_string = input()

while current_string != '0':
    list_with_strings.append(current_string)

    current_string = input()

min_string_len = float('inf')
min_string = None

for string in list_with_strings:
    if ' ' not in string and len(string) < min_string_len:
        min_string_len = len(string)
        min_string = string
        
print(f'Наименьшая длина: {min_string_len}\nСтрочка: {min_string}')