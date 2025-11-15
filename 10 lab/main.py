import time
from random import randint
from string import digits
from sys import exit

def shell_sort(array: list) -> tuple[list, int]:
    jump_size = len(array) // 2
    swaps = 0
    while jump_size > 0:
        for i in range(jump_size, len(array)):
            temp = array[i]
            temp_index = i
            while temp_index >= jump_size and array[temp_index - jump_size] > temp:
                array[temp_index] = array[temp_index - jump_size]
                temp_index -= jump_size
                swaps += 1
            array[temp_index] = temp
            if temp_index != i:
                swaps += 1
        jump_size //= 2
    return array, swaps


def sorting_algorithm_test(sizes: list[int], alghoritm = shell_sort) -> list[list[list[int]]]:
    time_of_each_size = []
    
    for test_size in sizes:
        time_of_each_size.append([])
        random_array = []
        for _ in range(test_size):
            random_array.append(randint(1, 100000))
            
        start_time = time.time()
        sort_array, swaps = shell_sort(random_array)
        end_time = time.time()
        time_of_each_size[-1].append([end_time - start_time, swaps])
        del random_array
        
        start_time = time.time()
        sort_array, swaps = shell_sort(sort_array)
        end_time = time.time()
        time_of_each_size[-1].append([end_time - start_time, swaps])
        
        reverse_sort_array = sort_array[::-1]
        del sort_array
        
        start_time = time.time()
        sort_array, swaps = alghoritm(reverse_sort_array)
        end_time = time.time()
        time_of_each_size[-1].append([end_time - start_time, swaps])
        
    return time_of_each_size

def string_to_int(s: str) -> int:
    is_negative = False
    current_number = ''
    for char in s:
        if char in digits:
            current_number += char
        elif not current_number and char == '-':
            is_negative = not is_negative
        else:
            exit('Ошибка: Введено неправильное число!')
    number = int('-'*is_negative + current_number)
    return number

def table_sort_visualize(test_data, sizes):
    rand_test, sort_test, reverse_test = zip(*test_data)
    n = 88
    table = '-' * n + '\n'
    table += f'|{'T\\N':^20}|{sizes[0]:^21.7g}|{sizes[1]:^21.7g}|{sizes[2]:^21.7g}|\n{'-' * n}\n'
    
    table += f'|{'':^20}|'
    for _ in range(3):
        table += f'{'время':^10}|{'перест.':^10}|'
    table += f'\n{'-' * n}\n'
    
    table += f'|{'Упоряд. список':^20}|'
    for i in sort_test:
        table += f'{i[0]:^10.5g}|{i[1]:^10.5g}|'
    table += f'\n{'-' * n}\n'
    
    table += f'|{'Случайный список':^20}|'
    for i in rand_test:
        table += f'{i[0]:^10.5g}|{i[1]:^10.5g}|'
    table += f'\n{'-' * n}\n'
    
    table += f'|{'Обр. упоряд. список':^20}|'
    for i in reverse_test:
        table += f'{i[0]:^10.5g}|{i[1]:^10.5g}|'
    table += f'\n{'-' * n}\n'
    print(table)

def graph_visualize(begin: int, end: int):
    number_of_sizes = 10
    number_of_serifs = 5
    size = 100
    step = (end - begin) / (number_of_sizes - 1)
    
    sizes = []
    for i in range(number_of_sizes):
        sizes.append(int(begin + i * step))
    coords = sorting_algorithm_test(sizes)
    
    max_time = coords[0][0][0]
    min_time = coords[0][0][0]
    for i in range(number_of_sizes):
        max_time = max(max_time, coords[i][0][0], coords[i][1][0], coords[i][2][0])
        min_time = min(min_time, coords[i][0][0], coords[i][1][0], coords[i][2][0])
    
    oneSerifSize = (max_time - min_time) / (number_of_serifs - 1)
    onePixelSize = (max_time - min_time) / size
    
    print('+ - рандомный списо\n'
          '~ - сортированный список\n'
          '* - обратно отсортированный список\n')

    s = ' ' * 6
    for i in range(number_of_serifs):
        currentSerif = min_time + i * oneSerifSize
        serifPosition = int((i * oneSerifSize) // onePixelSize)
        s += f'{' '*(serifPosition - len(s) + 5)}{currentSerif:^6.4g}'
    print(s)
    
    for i in range(number_of_sizes):
        rand_time, sort_time, reverse_time = coords[i][0][0], coords[i][1][0], coords[i][2][0]

        line = [' '] * (size + 1)
        
        rand_pos = int((rand_time - min_time) / onePixelSize)
        sort_pos = int((sort_time - min_time) / onePixelSize)
        reverse_pos = int((reverse_time - min_time) / onePixelSize)
        
        line[rand_pos] = '+'
        line[sort_pos] = '~'
        line[reverse_pos] = '*'
        
        print(f'{sizes[i]:^6.6g}|{''.join(line)}')

if __name__ == "__main__":
    array = list(map(string_to_int, input('Введите массив: ').split()))
    if len(array) == 0:
        exit('Ошибка: Массив не может быть пустым!')
    array, _ = shell_sort(array)
    print('Отсортированный список:', array)
    
    sizes_of_test = list(map(string_to_int, input('Введите 3 размерности для теста: ').split()))
    if len(sizes_of_test) != 3:
        exit('Ошибка: Неверное количество размеров!')
    
    test_data = sorting_algorithm_test(sizes_of_test)
    
    table_sort_visualize(test_data, sizes_of_test)
    
    input_values = list(map(string_to_int, input('Введите начальное и конечное значение: ').split()))
    
    if len(input_values) < 2:
        exit('Ошибка: Необходимо ввести 2 значения!')
    
    begin, end = input_values[0], input_values[1]
    
    if begin >= end:
        exit('Ошибка: Начальное значение должно быть меньше конечного!')
    
    if begin <= 0 or end <= 0:
        exit('Ошибка: Значения должны быть положительными!')
    
    graph_visualize(begin, end)
    