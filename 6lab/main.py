'''
Лаба 6
Иванов Андрей Александрович
ИУ7-16Б
'''

while True:
    command = input('''Выберите нужную команду из списка:
    1) Вставка элемента функцией пайтон
    2) Вставка алгоритмом
    3) Удалить элемент функцией пайтон
    4) Удалить элемент алгоритмом
    5) Нахождение К-го экстремума
    6) Наибольшая убывающая последовательность простых чисел
    7) Поменять местами наибольший отрицательный и последний нулевой
    0) Закончить выполнение команды
    Команда: ''')

    match command:
        
        case '1':
            exec(open('6lab\\func1.py', encoding='utf-8').read())
            
        case '2':
            exec(open('6lab\\func2.py', encoding='utf-8').read())
            
        case '3':
            exec(open('6lab\\func3.py', encoding='utf-8').read())
            
        case '4':
            exec(open('6lab\\func4.py', encoding='utf-8').read())
            
        case '5':
            exec(open('6lab\\func5.py', encoding='utf-8').read())
            
        case '6':
            exec(open('6lab\\func6.py', encoding='utf-8').read())
            
        case '7':
            exec(open('6lab\\func7.py', encoding='utf-8').read())
            
        case '0':
            break
         
        case _:
            print('Неверный ввод команды')