'''
Иванов Андрей
Иу7-16Б
Лаба 11 (часть 2)
'''
from typing import Callable
from sys import exit
from main import simpson_3_8, float_input, EPS


def f(x: float) -> float:
    return x ** 2


def g(x: float) -> float:
    return -x ** 2 + 2


def find_intersections(f: Callable, g: Callable, 
                       start: float = -20, end: float = 20, 
                       step: float = 2, epsilon: float = 1e-6) -> list[float]:
    intersections = []
    x = start
    
    while x < end:
        x_next = min(x + step, end)
        
        if (f(x) - g(x)) * (f(x_next) - g(x_next)) < 0:
            a, b = x, x_next
            iterations = 0
            
            while (b - a) / 2 > epsilon and iterations < 1000:
                c = (a + b) / 2
                if abs(f(c) - g(c)) < epsilon:
                    intersections.append(c)
                    break
                if (f(a) - g(a)) * (f(c) - g(c)) < 0:
                    b = c
                else:
                    a = c
                iterations += 1
            else:
                intersections.append((a + b) / 2)
        
        x = x_next
    
    return intersections


def calculate_area(f: Callable, g: Callable, x1: float, x2: float, 
                  epsilon: float = 1e-6) -> tuple:
    
    def area_func(x):
        return abs(f(x) - g(x))
    
    n = 3
    prev_area = 0
    iterations = 0
    max_iterations = 100
    
    while iterations < max_iterations:
        area = simpson_3_8(area_func, x1, x2, n)
        if abs(area - prev_area) < epsilon and iterations > 0:
            return area, n
        prev_area = area
        n += 3
        iterations += 1
    
    return prev_area, n


def graph_visualize(f: Callable, g: Callable, prime_begin: float = -20, prime_end: float = 20, intersections: bool = False):
    number_of_serifs = 5
    size = 120
    begin, end = prime_begin - 1, prime_end + 1
    step_x = (end - begin) / 40
    
    f_coords = []
    g_coords = []
    x_coords = []
    func_max = float('-inf')
    func_min = float('inf')
    
    x = begin
    while x <= end:
        current_f = f(x)
        current_g = g(x)
        
        f_coords.append(current_f)
        g_coords.append(current_g)
        x_coords.append(x if abs(x) > EPS else 0)

        func_max = max(func_max, current_f, current_g)
        func_min = min(func_min, current_f, current_g)
        
        x += step_x
    
    onePixelSize = (func_max - func_min) / size
    oneSerifSize = (func_max - func_min) / (number_of_serifs - 1)
    
    print('F - Функция f\n'
          'G - Функция g\n'
          '* - Площадь внутри фигуры\n')

    s = ' ' * 6
    for i in range(number_of_serifs):
        currentSerif = func_min + i * oneSerifSize
        serifPosition = int((i * oneSerifSize) / onePixelSize)
        s += f'{" " * (serifPosition - len(s) + 6)}{currentSerif:^6.4g}'
    print(s)
    
    for i in range(len(x_coords)):
        current_f = f_coords[i]
        current_g = g_coords[i]
        x = x_coords[i]
        
        line = [' '] * (size + 1)
        
        f_pos = int((current_f - func_min) / onePixelSize)
        g_pos = int((current_g - func_min) / onePixelSize)
        
        f_pos = max(0, min(size, f_pos))  
        g_pos = max(0, min(size, g_pos))  
        
        if intersections and prime_begin <= x <= prime_end:
            a, b = sorted((f_pos, g_pos))
            for j in range(a, b + 1):
                if 0 <= j <= size:
                    line[j] = '░'
        
        line[f_pos] = 'F'
        line[g_pos] = 'G'
            
        print(f'{x:^8.5g}|{"".join(line)}')

if __name__ == '__main__':
    epsilon_input = input(f'Введите точность E (по умолчанию {EPS}): ').strip()
    epsilon = float_input(epsilon_input) if epsilon_input else EPS
    
    if epsilon <= 0:
        exit('Ошибка: точность должна быть положительной!')
    
    intersections = find_intersections(f, g, epsilon=epsilon)
    
    if len(intersections) < 2:
        print(intersections)
        graph_visualize(f, g)
        exit('Ошибка: недостаточно точек пересечения!')
    
    print(f'Найдено точек пересечения: {len(intersections)}')
    for i, x in enumerate(intersections, 1):
        print(f'  Точка {i}: x = {x:<.7g}, y = {f(x):<.7g}')
    
    print('-' * 80)
    x1, x2 = intersections[0], intersections[1]
    area, n = calculate_area(f, g, x1, x2, epsilon)
    print(f'Площадь фигуры: {area}')
    
    graph_visualize(f, g, x1, x2, True)