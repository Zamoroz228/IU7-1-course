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
    os.chdir(path)
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
                return os.path.join(path, a)
            print(f'Ошибка: {error}')


def decode_line(line: str, delimetr: str = ';') -> list[str]:
    fields = []
    current_field = ''
    i = 0
    n = len(line)
    while i < n:
        char = line[i]
        if char == '"':
            i += 1
            while i < n:
                if line[i] == '"':
                    if i + 1 < n and line[i + 1] == '"':
                        current_field += '"'
                        i += 2
                    else:
                        i += 1
                        break
                else:
                    current_field += line[i]
                    i += 1  
        elif char == delimetr:
            fields.append(current_field)
            current_field = ''
            i += 1
        elif char == '\n':
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
            field = field.replace('"', '""')
            field = '"' + field + '"'
        line += field + ';'
    return line[:-1]


def decode_types(line: str):
    types = []
    all_types_dict = {
        "<class 'str'>": str,
        "<class 'bool'>": bool,
        "<class 'int'>": int,
        "<class 'float'>": float
    }
    for t in decode_line(line):
        t = t.strip()
        real_type = all_types_dict.get(t)
        if real_type is None:
            raise ValueError('Неправильный тип данных')
        else:
            types.append(real_type)
    return types


def read_title(path: str) -> tuple[list[str], list[type]]:
    with open(path, 'r', encoding='utf-8') as file:
        title = decode_line(file.readline())
        types = decode_types(file.readline())
        if len(title) != len(types):
            raise ValueError('Не совпадает количество столбцов и типов данных')
        return title, types


def create_standart_table(path: str) -> tuple[list[str], list[type]]:
    title = ['Имя', 'Фамилия', 'Рост', 'Возраст', 'Вес']
    types = [str, str, float, int, float]
    with open(path, 'w', encoding='utf-8') as file:
        file.write(encode_line(title) + '\n' + encode_line(types) + '\n')
    return title, types
    
    
def create_table(path: str) -> tuple[list[str], list[type]]:
    title = input('Введите названия столбцов через пробел: ').split()
    types = []
    for name in title:
        while True:
            print('-' * 50)
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
        file.write(encode_line(title) + '\n' + encode_line(types) + '\n')
    return title, types


def check_line(fields: list, types: list[type]) -> bool:
    if len(fields) != len(types):
        print('Количество введенных данных не соотвествует количеству столбцов')
        return False
    
    for i in range(len(fields)):
        try:
            if types[i] == bool:
                if fields[i].lower() == 'true':
                    fields[i] = True
                elif fields[i].lower() == 'false':
                    fields[i] = False
                else:
                    print(f'Не соотвествующий тип данных {fields[i]}, ожидалось {types[i]}')
                    return False
            else:
                fields[i] = types[i](fields[i])
        except (ValueError, TypeError):
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


def conditionals(title: list[str], types: list[type]) -> list[str]:
    cond = [''] * len(title)
    while True:
        print('Все столбцы')
        [print(f'{i}) {title[i]}') for i in range(len(title))]
        try:
            _a = input('Введите номер нужного: ')
            if not _a:
                break
            a = int(_a)
        except ValueError:
            print('Введенно не числовая строка')
            continue
        if not 0 <= a < len(title) or cond[a]:
            print('Выбран неправильный номер или для этой строчки уже есть условие')
            continue
        
        t = types[a]
        match str(t):
            case "<class 'int'>" | "<class 'float'>":
                print('Введите выражение по типу 10 / 3 <= x < 1.000.000')
                express = input('Ваше выражение: ')
                try: 
                    x = 0
                    eval(express)
                except Exception:
                    print('Неверно введено выражение')
                    continue
            case "<class 'bool'>":
                express = 'x ==' + input('Введите либо True либо False: ')
                try:
                    x = True
                    eval(express)
                except Exception:
                    print('Неверно введено выражение')
                    continue
            case "<class 'str'>": 
                print("Введите выражение по типу len(x) > 10 или 'yes' in x")
                express = input('Ваше выражение: ')
                try:
                    x = '123'
                    eval(express)
                except Exception:
                    print('Неверно введено выражение')
                    continue
            case _:
                raise ValueError('Неправильный тип данных')
            
        cond[a] = express
        
    return cond        
    

def test_fields(fields: list, cond: list[str]) -> bool:
    for i in range(len(fields)):
        if not cond[i]:
            continue
        x = fields[i]
        if not eval(cond[i]):
            return False
    return True 
    
                    
def read_table(path: str, with_conditional: bool = False):
    with open(path, 'r', encoding='utf-8') as file:
        title, types = decode_line(file.readline()), decode_types(file.readline())
        if len(title) != len(types):
            raise ValueError('Не совпадает количество столбцов и типов данных')
        if with_conditional:
            cond = conditionals(title, types)
        print(' '.join(title))
        for line in file:
            fields = decode_line(line)
            text_fields = fields.copy()
            check_line(fields, types)
            if with_conditional:
                if test_fields(fields, cond):
                    print(' '.join(text_fields))
            else:
                print(' '.join(text_fields))


def sorting_table(path: str):
    with open(path, 'r', encoding='utf-8') as file:
        title, types = decode_line(file.readline()), decode_types(file.readline())
        if len(title) != len(types):
            raise ValueError('Не совпадает количество столбцов и типов данных')
        [print(f'{i}) {title[i]}') for i in range(len(title))]
        while True:
            try:
                columns = list(map(int, input('Нужные столбцы в порядке приоритета: ').split()))        
            except ValueError:
                print('Все значение должны быть int')
                continue
            if min(columns) < 0 or max(columns) >= len(title):
                print('Значения не соотвествуют столбцам')
                continue
            break
        keys_value = []
        while True:
            pos = file.tell()
            line = file.readline()
            if not line:
                break
            fields = decode_line(line)
            check_line(fields, types)
            keys_value.append(list())
            for column in columns:
                keys_value[-1].append(fields[column])
            
            keys_value[-1].append(pos)
            
        keys_value.sort()
        directory, file_name = os.path.split(path)
        new_path = os.path.join(directory, '_' + file_name)
        with open(new_path, 'w', encoding='utf-8') as file2:
            file2.write(encode_line(title) + '\n' + encode_line(types) + '\n')
            for *_, index in keys_value:
                file.seek(index)
                file2.write(file.readline())
    os.remove(path)
    os.rename(new_path, path)


def main():
    path = select_path()
    while True:
        print('Команды:')
        print('1) Инициализировать бд')
        print('2) Дополнить данными бд')
        print('3) Вывести бд')
        print('4) Поиск с фильтрами по бд')
        print('5) Отсортировать бд')
        print('6) Сменить путь')
        print('0) Выход из программы')
        print('Команды:')
        a = input('Введите номер нужнйо комманды: ')
        match a:
            case '1':
                answer = input('Вы хотите cоздать пользователскую структуру (yes/no): ')
                match answer:
                    case 'yes':
                        title, types = create_table(path)
                    case 'no':
                        title, types = create_standart_table(path)
                    case _:
                        print('Неправильная команды')
                        continue
                fill_table(path, title, types)
            case '2':
                try:
                    fill_table(path)
                except (ValueError, FileNotFoundError) as err:
                    print(f'База данных пустая или такого файла не существует {err}')
            case '3':
                try:
                    read_table(path)
                except (ValueError, FileNotFoundError) as err:
                    print(f'База данных пустая или такого файла не существует {err}')
            case '4':
                try:
                    read_table(path, True)
                except (ValueError, FileNotFoundError) as err:
                    print(f'База данных пустая или такого файла не существует {err}')
            case '5':
                try:
                    sorting_table(path)
                except (ValueError, FileNotFoundError) as err:
                    print(f'База данных пустая или такого файла не существует {err}')
            case '6':
                path = select_path()
            case '0':
                raise KeyboardInterrupt
            case _:
                print('Неправильная команды')
                continue
            
            
if __name__ == '__main__':
    try: 
        main()
    except KeyboardInterrupt:
        print('Программа завершена')