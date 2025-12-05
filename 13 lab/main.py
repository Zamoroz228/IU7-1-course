from dataclasses import fields
import os

def select_path():
    while True:
        path = input('Введите нужную стартовую папку (выбор текущей пустая строка): ')
        if not path:
            path = os.path.abspath(os.curdir)
            break
        elif os.path.isdir(path):
            break
        elif os.path.splitext(path)[-1] == '.csv':
            return path
        print('Неправильно введен путь, попробуй еще раз!')
    print(f'Отлично, выбран путь: {path}')
    while True:
        try:
            print('-' * 50)
            [print(i) for i in os.listdir(path)]
            a = input()
            os.chdir(a)
            path = os.path.abspath(os.curdir)
            print('-' * 50)
            print(path)
        except (FileNotFoundError, NotADirectoryError, OSError) as error:
            if os.path.splitext(a)[-1] == '.csv':
                return path + '\\' + a
            print(f'Ошибка: {error}')


def decode_line(line: str, delimetr: str = ';') -> list[str]:
    fields = []
    current_field = ''
    i = 0
    while i < len(line):
        char = line[i]
        if char == '"':
            i += 1
            if line[i] == '"':
                current_field += '"'
                i += 1
            else:
                while line[i] != '"':
                    current_field += line[i]
                    i += 1
                i += 1
        elif char in delimetr:
            fields.append(current_field)
            current_field = ''
            i += 1
        else:
            current_field += char
            i += 1
    fields.append(current_field)
    
    return fields
            
             
def encode_line(fields: list, delimetr: str = ';'):
    line = ''
    for field in fields:
        field = str(field)
        if delimetr in field or '"' in field:
            field.replace('"', '""')
            field.replace(delimetr, f'"{delimetr}"')
        line += field + ';'
    return line[:-1]


def decode_types(line: str):
    types = []
    for t in decode_line(line):
        t = t.strip()
        match t:
            case "<class 'str'>":
                types.append(str)
            case "<class 'bool'>":
                types.append(bool)
            case "<class 'int'>":
                types.append(int)
            case "<class 'float'>":
                types.append(float)
            case _:
                raise ValueError(f'Ошибка тип данных {t}')
    return types


def read_title(path: str) -> tuple[list[str], list[type]]:
    with open(path, 'r', encoding='utf-8') as file:
        title = decode_line(file.readline())
        types = decode_types(file.readline())
        return title, types


def create_table(path: str) -> tuple[list[str], list[type]]:
    title = input('Введите названия столбцов через пробел: ').split()
    types = []
    for name in title:
        while True:
            print('1) str')
            print('2) bool')
            print('3) int')
            print('4) float')
            a = input(f'Введите нужный тип данных для столбца {name}: ')
            match a:
                case '1':
                    types.append(str)
                case '2':
                    types.append(bool)
                case '3':
                    types.append(int)
                case '4':
                    types.append(float)
                case _:
                    print('Неправильный формат данных!')
                    continue
            break
    with open(path, 'w', encoding='utf-8') as file:
        file.write(encode_line(title) + '\n' + encode_line(types))
    return title, types


def check_line(fields: list[str], types: list[type]) -> bool:
    if len(fields) != len(types):
        print('Количество введенных данных не соотвествует количеству столбцов')
        return False
    
    for i in range(len(fields)):
        try:
            fields[i] = types[i](fields[i])
        except:
            print(f'Не соотвествующий тип данных {fields[i]}, ожидалось {types[i]}')
            return False
    
    return True


def fill_table(path: str, title: list[str] = None, types: list[type] = None): # type: ignore
    if title is None or types is None:
        title, types = read_title(path)
        
    with open(path, 'a', encoding='utf-8') as file:
        t = 0 
        while True:
            if t % 5 == 0:
                t += 1
                print('Названия столбцов:', ' '.join(title))
            a = input(f'Введите одну строчку через пробел, введите пустую строчку для конца ввода: ')
            if not a:
                break
            fields = a.split()
            if check_line(fields, types):
                file.write(encode_line(fields) + '\n')
                    
def read_table(path: str):
    with open(path, 'r', encoding='utf-8') as file:
        title, types = decode_line(file.readline()), decode_types(file.readline())
        print(' '.join(title), end='')
        for line in file:
            fields = decode_line(line)
            print(' '.join(fields), end='')
            check_line(fields, types)


def main():
    pass
    
            
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Программа завершена')