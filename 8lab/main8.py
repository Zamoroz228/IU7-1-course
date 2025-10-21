'''
Лаба 8
Иванов Андрей Александрович
ИУ7-16Б
Варианты 4 5
'''

from subprocess import run
from sys import executable

while True:
    command = input(open('./8lab/begin_text.txt', encoding='utf-8').read())

    match command:
        
        case '1':
            run([executable, './8lab/1.py'])

        case '2':
            run([executable, './8lab/2.py'])

        case '3':
            run([executable, './8lab/3.py'])

        case '4':
            run([executable, './8lab/4.py'])
            
        case '5':
            run([executable, './8lab/5.py'])

        case '6':
            run([executable, './8lab/6.py'])
            
        case '0':
            break
        
        case _:
            print('Неверный ввод команды')