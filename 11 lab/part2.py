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
    return -x ** 2 + 4


def find_intersections(f: Callable, g: Callable, 
                       start: float = -20, end: float = 20, 
                       step: float = 2, epsilon: float = 1e-6) -> list:
    """
    Поиск точек пересечения двух функций методом бисекции
    
    Параметры:
    f, g - функции для поиска пересечений
    start, end - границы области поиска
    step - шаг для поиска отрезков со сменой знака
    epsilon - требуемая точность
    
    Возвращает: список точек пересечения [x1, x2, ...]
    """
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
    """
    Вычисление площади фигуры между графиками методом Симпсона 3/8
    
    Параметры:
    f, g - функции
    x1, x2 - точки пересечения (границы интегрирования)
    epsilon - требуемая точность
    
    Возвращает: (площадь фигуры, количество разбиений)
    """
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


def graph_visualize(f: Callable, g: Callable, intersections: list, 
                   area: float, x_start: float = None, x_end: float = None) -> None:
    """
    Визуализация графиков функций и закрашенной области
    
    Параметры:
    f, g - функции
    intersections - список точек пересечения
    area - площадь фигуры
    x_start, x_end - границы отображения по X
    """
    width = 100
    height = 30
    
    if len(intersections) >= 2:
        area_start = min(intersections[0], intersections[1])
        area_end = max(intersections[0], intersections[1])
        
        if x_start is None or x_end is None:
            x_margin = abs(area_end - area_start) * 0.5
            x_start = area_start - x_margin
            x_end = area_end + x_margin
    else:
        area_start = area_end = None
        if x_start is None:
            x_start = -20
        if x_end is None:
            x_end = 20
    
    num_points = width
    x_values = []
    f_values = []
    g_values = []
    
    for i in range(num_points):
        x = x_start + (x_end - x_start) * i / (num_points - 1)
        x_values.append(x)
        try:
            f_val = f(x)
            g_val = g(x)
            f_values.append(f_val)
            g_values.append(g_val)
        except:
            f_values.append(0)
            g_values.append(0)
    
    all_values = f_values + g_values
    y_min = min(all_values)
    y_max = max(all_values)
    y_range = y_max - y_min
    
    if y_range > EPS:
        y_min -= y_range * 0.1
        y_max += y_range * 0.1
        y_range = y_max - y_min
    else:
        y_min -= 1
        y_max += 1
        y_range = 2
    
    grid = [[' ' for _ in range(width)] for _ in range(height)]
    
    # Ось X (y=0)
    if y_min <= 0 <= y_max:
        y_zero = int((y_max - 0) / y_range * (height - 1))
        for i in range(width):
            if 0 <= y_zero < height:
                grid[y_zero][i] = '-'
    
    # Ось Y (x=0)
    if x_start <= 0 <= x_end:
        x_zero = int((0 - x_start) / (x_end - x_start) * (width - 1))
        for i in range(height):
            if 0 <= x_zero < width:
                if grid[i][x_zero] == '-':
                    grid[i][x_zero] = '+'
                else:
                    grid[i][x_zero] = '|'
    
    # Закрашиваем область между графиками
    if area_start is not None and area_end is not None:
        for i in range(width):
            x = x_values[i]
            if area_start <= x <= area_end:
                try:
                    y_f = f(x)
                    y_g = g(x)
                    y_top = max(y_f, y_g)
                    y_bottom = min(y_f, y_g)
                    
                    pixel_top = int((y_max - y_top) / y_range * (height - 1))
                    pixel_bottom = int((y_max - y_bottom) / y_range * (height - 1))
                    
                    for j in range(max(0, pixel_top), min(height, pixel_bottom + 1)):
                        if grid[j][i] in [' ', '-', '|']:
                            grid[j][i] = '░'
                except:
                    pass
    
    # Рисуем графики функций
    for i in range(num_points):
        if f_values[i] is not None:
            y_pixel = int((y_max - f_values[i]) / y_range * (height - 1))
            if 0 <= y_pixel < height:
                if grid[y_pixel][i] in [' ', '░', '-']:
                    grid[y_pixel][i] = 'f'
                elif grid[y_pixel][i] == '|':
                    grid[y_pixel][i] = 'f'
        
        if g_values[i] is not None:
            y_pixel = int((y_max - g_values[i]) / y_range * (height - 1))
            if 0 <= y_pixel < height:
                if grid[y_pixel][i] == 'f':
                    grid[y_pixel][i] = 'X'
                elif grid[y_pixel][i] in [' ', '░', '-']:
                    grid[y_pixel][i] = 'g'
                elif grid[y_pixel][i] == '|':
                    grid[y_pixel][i] = 'g'
    
    # Отмечаем точки пересечения
    for x_int in intersections:
        if x_start <= x_int <= x_end:
            x_pixel = int((x_int - x_start) / (x_end - x_start) * (width - 1))
            try:
                y_int = f(x_int)
                y_pixel = int((y_max - y_int) / y_range * (height - 1))
                if 0 <= x_pixel < width and 0 <= y_pixel < height:
                    grid[y_pixel][x_pixel] = '*'
            except:
                pass
    
    print('\n' + '=' * width)
    print('ГРАФИК ФУНКЦИЙ'.center(width))
    print('=' * width)
    print(f'f(x) = x²,  g(x) = -x² + 4')
    print(f'Площадь фигуры: {area:.7g}')
    print('=' * width)
    print('\nЛегенда:')
    print('  f - график f(x)')
    print('  g - график g(x)')
    print('  * - точки пересечения')
    print('  ░ - площадь фигуры')
    print('  X - пересечение графиков в данной точке')
    print()
    
    print(f'Y = {y_max:7.3g}')
    for row in grid:
        print(''.join(row))
    print(f'Y = {y_min:7.3g}')
    
    num_x_labels = 5
    x_label_line = ''
    for i in range(num_x_labels):
        x_val = x_start + (x_end - x_start) * i / (num_x_labels - 1)
        position = int(i * (width - 1) / (num_x_labels - 1))
        label = f'{x_val:7.3g}'
        if i == 0:
            x_label_line = label
        else:
            spaces_needed = position - len(x_label_line)
            x_label_line += ' ' * spaces_needed + label
    print(x_label_line)
    print('=' * width + '\n')


def print_results_table(intersections: list, area: float, n: int) -> None:
    """
    Вывод таблицы с результатами
    
    Параметры:
    intersections - точки пересечения
    area - площадь фигуры
    n - количество разбиений
    """
    width = 70
    print('=' * width)
    print('РЕЗУЛЬТАТЫ ВЫЧИСЛЕНИЙ'.center(width))
    print('=' * width)
    
    print(f'\n{"Точки пересечения:":.<40}')
    for i, x in enumerate(intersections, 1):
        y = f(x)
        print(f'  Точка {i}: x = {x:10.7g}, y = {y:10.7g}')
    
    if len(intersections) >= 2:
        x1, x2 = intersections[0], intersections[1]
        print(f'\n{"Границы интегрирования:":.<40}')
        print(f'  От x = {min(x1, x2):10.7g}')
        print(f'  До x = {max(x1, x2):10.7g}')
        print(f'  Длина отрезка: {abs(x2 - x1):10.7g}')
    
    print(f'\n{"Метод вычисления:":.<40} Симпсона 3/8')
    print(f'{"Количество разбиений (N):":.<40} {n}')
    print(f'{"Площадь фигуры:":.<40} {area:.7g}')
    print('=' * width + '\n')



if __name__ == '__main__':
    """Главная функция программы"""
    print('=' * 80)
    print('ЛАБОРАТОРНАЯ РАБОТА 11 (ЧАСТЬ 2)'.center(80))
    print('=' * 80)
    print('Программа для поиска площади фигуры, ограниченной графиками функций'.center(80))
    print('=' * 80)
    print('\nФункции:')
    print('  f(x) = x²')
    print('  g(x) = -x² + 4')
    print('\nОбласть поиска пересечений: [-20, 20]')
    print('Метод поиска корней: половинное деление')
    print('Метод интегрирования: Симпсона 3/8')
    print('=' * 80 + '\n')
    
    epsilon_input = input(f'Введите точность ε (по умолчанию {EPS}): ').strip()
    epsilon = float_input(epsilon_input) if epsilon_input else EPS
    
    if epsilon <= 0:
        exit('Ошибка: точность должна быть положительной!')
    
    print(f'\nИспользуется точность: {epsilon}')
    
    print('\n' + '-' * 80)
    print('Поиск точек пересечения методом половинного деления')
    print('-' * 80)
    
    intersections = find_intersections(f, g, epsilon=epsilon)
    
    if len(intersections) < 2:
        print(f'Недостаточно точек пересечения для вычисления площади')
        print(f'Найдено: {len(intersections)}')
        if intersections:
            for i, x in enumerate(intersections, 1):
                print(f'  Точка {i}: x = {x:.7g}, y = {f(x):.7g}')
        exit('Ошибка: недостаточно точек пересечения!')
    
    print(f'Найдено точек пересечения: {len(intersections)}')
    for i, x in enumerate(intersections, 1):
        print(f'  Точка {i}: x = {x:.7g}, y = {f(x):.7g}')
    
    print('\n' + '-' * 80)
    print('Вычисление площади фигуры методом Симпсона 3/8')
    print('-' * 80)
    x1, x2 = intersections[0], intersections[1]
    area, n = calculate_area(f, g, x1, x2, epsilon)
    
    print_results_table(intersections, area, n)
    
    graph_visualize(f, g, intersections, area)