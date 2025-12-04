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
            if os.path.splitext(path)[-1] == '.csv':
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


def main():
    path = select_path()
    with open(path, 'w', encoding='utf-8') as file:
        while True:
            line = encode_line(input().split())
            if not line:
                break
            file.write(line + '\n')
            
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Программа завершена') 