'''
Лаба 6
Иванов Андрей Александрович
ИУ7-16Б
'''

while True:
    command = input('''Выберите нужную команду из списка:
    1a) Вставка элемента функцией пайтон
    1b) Вставка алгоритмом
    2a) Удалить элемент функцией пайтон
    2b) Удалить элемент алгоритмом
    3) Нахождение К-го экстремума
    4) Наибольшая убывающая последовательность простых чисел
    5) Поменять местами наибольший отрицательный и последний нулевой
    0) Закончить выполнение команды
    Команда: ''')

    match command:
        
        case '1a':
            exec(open('6lab\\func1a.py', encoding='utf-8').read())
            
        case '1b':
            exec(open('6lab\\func1b.py', encoding='utf-8').read())
            
        case '2a':
            exec(open('6lab\\func2a.py', encoding='utf-8').read())
            
        case '2b':
            exec(open('6lab\\func2b.py', encoding='utf-8').read())
            
        case '3':
            exec(open('6lab\\func3.py', encoding='utf-8').read())
            
        case '4':
            exec(open('6lab\\func4.py', encoding='utf-8').read())
            
        case '5':
            exec(open('6lab\\func5.py', encoding='utf-8').read())
            
        case '0':
            break
         
        case _:
            print('Неверный ввод команды')