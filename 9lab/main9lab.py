'''
Лаба 9
Иванов Андрей Александрович
ИУ7-16Б
'''

from subprocess import run
from sys import executable

text = open('./9lab/begin_text.txt', encoding='utf-8').read()
while True:
    command = input(text)

    match command:
        
        case '1':
            run([executable, './9lab/1.py'])

        case '2':
            run([executable, './9lab/2.py'])

        case '3':
            run([executable, './9lab/3.py'])

        case '4':
            run([executable, './9lab/4.py'])
            
        case '5':
            run([executable, './9lab/5.py'])

        case '6':
            run([executable, './9lab/6.py'])

        case '7':
            run([executable, './9lab/7.py'])
            
        case '0':
            break
        
        case _:
            print('Неверный ввод команды')