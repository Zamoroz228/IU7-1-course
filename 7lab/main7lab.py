'''
Лаба 7
Иванов Андрей Александрович
ИУ7-16Б
Варианты 4 2 7 5
'''

while True:
    command = input(open('./7lab/begin_text.txt', encoding='utf-8').read())

    match command:
        
        case '1':
            exec(open('./7lab/1.py', encoding='utf-8').read())
            
        case '2':
            exec(open('./7lab/2.py', encoding='utf-8').read())
                
        case '3':
            exec(open('./7lab/3.py', encoding='utf-8').read())
            
        case '4':
            exec(open('./7lab/4.py', encoding='utf-8').read())
            
        case '0':
            break
         
        case _:
            print('Неверный ввод команды')