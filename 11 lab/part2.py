'''
Иванов Андрей
Иу7-16Б
Лаба 11 (часть 2)
Программа для поиска точек пересечения двух функций
и вычисления площади замкнутой фигуры
'''
from typing import Callable
from sys import exit

# Импорт функций из первой части лабораторной работы
from main import simpson_3_8, float_input, EPS


def f(x: float) -> float:
    """Первая функция: f(x) = x²"""
    return x ** 2


def g(x: float) -> float:
    """Вторая функция: g(x) = x + 2"""
    return -x**2 + 2


def bisection_method(func: Callable, a: float, b: float, epsilon: float = 1e-6) -> float:
    """
    Метод половинного деления для поиска корня функции
    
    Параметры:
    func - функция, корень которой ищем
    a, b - границы отрезка
    epsilon - требуемая точность
    
    Возвращает: приближенное значение корня
    """
    if func(a) * func(b) > 0:
        raise ValueError("На концах отрезка функция должна иметь разные знаки")
    
    iterations = 0
    max_iterations = 1000
    
    while (b - a) / 2 > epsilon and iterations < max_iterations:
        c = (a + b) / 2
        if abs(func(c)) < epsilon:
            return c
        if func(a) * func(c) < 0:
            b = c
        else:
            a = c
        iterations += 1
    
    return (a + b) / 2


def find_intersection_segments(f: Callable, g: Callable, 
                               start: float = -20, end: float = 20, 
                               step: float = 2) -> list:
    """
    Поиск отрезков, на которых функции пересекаются
    
    Параметры:
    f, g - функции
    start, end - границы области поиска
    step - шаг исследования
    
    Возвращает: список отрезков [(a1, b1), (a2, b2), ...]
    """
    segments = []
    x = start
    
    def diff(x):
        return f(x) - g(x)
    
    while x < end:
        x_next = min(x + step, end)
        # Проверяем смену знака
        if diff(x) * diff(x_next) < 0:
            segments.append((x, x_next))
        x = x_next
    
    return segments


def find_intersections(f: Callable, g: Callable, epsilon: float = 1e-6) -> list:
    """
    Поиск точек пересечения двух функций
    
    Параметры:
    f, g - функции
    epsilon - требуемая точность
    
    Возвращает: список точек пересечения [x1, x2, ...]
    """
    # Находим отрезки, где функции пересекаются
    segments = find_intersection_segments(f, g)
    
    if not segments:
        return []
    
    # Для каждого отрезка находим точную точку пересечения
    intersections = []
    
    def diff(x):
        return f(x) - g(x)
    
    for a, b in segments:
        try:
            root = bisection_method(diff, a, b, epsilon)
            intersections.append(root)
        except ValueError:
            continue
    
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
    
    # Итерационно увеличиваем n до достижения точности
    n = 3
    prev_area = 0
    iterations = 0
    max_iterations = 100
    
    while iterations < max_iterations:
        try:
            area = simpson_3_8(area_func, x1, x2, n)
            if abs(area - prev_area) < epsilon and iterations > 0:
                return area, n
            prev_area = area
            n += 3  # Увеличиваем на 3, чтобы сохранить кратность
            iterations += 1
        except ValueError:
            n += 3
    
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
    width = 100  # Ширина графика в символах
    height = 30  # Высота графика в символах
    
    # Определяем границы области интегрирования
    if len(intersections) >= 2:
        area_start = min(intersections[0], intersections[1])
        area_end = max(intersections[0], intersections[1])
        
        # Автоматически определяем границы отображения
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
    
    # Вычисляем значения функций для определения диапазона Y
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
    
    # Определяем диапазон Y
    all_values = f_values + g_values
    y_min = min(all_values)
    y_max = max(all_values)
    y_range = y_max - y_min
    
    # Добавляем отступы
    if y_range > EPS:
        y_min -= y_range * 0.1
        y_max += y_range * 0.1
        y_range = y_max - y_min
    else:
        y_min -= 1
        y_max += 1
        y_range = 2
    
    # Создаем сетку графика
    grid = [[' ' for _ in range(width)] for _ in range(height)]
    
    # Рисуем оси
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
        # График f(x)
        if f_values[i] is not None:
            y_pixel = int((y_max - f_values[i]) / y_range * (height - 1))
            if 0 <= y_pixel < height:
                if grid[y_pixel][i] in [' ', '░', '-']:
                    grid[y_pixel][i] = 'f'
                elif grid[y_pixel][i] == '|':
                    grid[y_pixel][i] = 'f'
        
        # График g(x)
        if g_values[i] is not None:
            y_pixel = int((y_max - g_values[i]) / y_range * (height - 1))
            if 0 <= y_pixel < height:
                if grid[y_pixel][i] == 'f':
                    grid[y_pixel][i] = 'X'  # Пересечение графиков
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
    
    # Выводим график
    print('\n' + '=' * width)
    print('ГРАФИК ФУНКЦИЙ'.center(width))
    print('=' * width)
    print(f'f(x) = x²,  g(x) = x + 2')
    print(f'Площадь фигуры: {area:.7g}')
    print('=' * width)
    print('\nЛегенда:')
    print('  f - график f(x)')
    print('  g - график g(x)')
    print('  * - точки пересечения')
    print('  ░ - площадь фигуры')
    print('  X - пересечение графиков в данной точке')
    print()
    
    # Верхняя граница Y
    print(f'Y = {y_max:7.3g}')
    
    # Выводим сетку
    for row in grid:
        print(''.join(row))
    
    # Нижняя граница Y
    print(f'Y = {y_min:7.3g}')
    
    # Шкала X
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


def main():
    """Главная функция программы"""
    print('=' * 80)
    print('ЛАБОРАТОРНАЯ РАБОТА 11 (ЧАСТЬ 2)'.center(80))
    print('=' * 80)
    print('Программа для поиска площади фигуры, ограниченной графиками функций'.center(80))
    print('=' * 80)
    print('\nФункции:')
    print('  f(x) = x²')
    print('  g(x) = x + 2')
    print('\nОбласть поиска пересечений: [-20, 20]')
    print('Метод поиска корней: половинное деление')
    print('Метод интегрирования: Симпсона 3/8')
    print('=' * 80 + '\n')
    
    # Ввод точности
    epsilon_input = input(f'Введите точность ε (по умолчанию {EPS}): ').strip()
    if epsilon_input:
        try:
            epsilon = float_input(epsilon_input)
            if epsilon <= 0:
                exit('Ошибка: точность должна быть положительной!')
        except:
            exit('Ошибка при вводе точности!')
    else:
        epsilon = EPS
    
    print(f'\nИспользуется точность: {epsilon}')
    
    # Поиск точек пересечения
    print('\n' + '-' * 80)
    print('ШАГ 1: Поиск отрезков, содержащих точки пересечения')
    print('-' * 80)
    segments = find_intersection_segments(f, g)
    
    if not segments:
        print('Функции не пересекаются на отрезке [-20, 20]')
        return
    
    print(f'Найдено отрезков: {len(segments)}')
    for i, (a, b) in enumerate(segments, 1):
        print(f'  Отрезок {i}: [{a:6.3g}, {b:6.3g}]')
    
    # Поиск точных точек пересечения
    print('\n' + '-' * 80)
    print('ШАГ 2: Поиск точных точек пересечения методом половинного деления')
    print('-' * 80)
    intersections = find_intersections(f, g, epsilon)
    
    if len(intersections) < 2:
        print(f'Недостаточно точек пересечения для вычисления площади')
        print(f'Найдено: {len(intersections)}')
        if intersections:
            for i, x in enumerate(intersections, 1):
                print(f'  Точка {i}: x = {x:.7g}, y = {f(x):.7g}')
        return
    
    print(f'Найдено точек пересечения: {len(intersections)}')
    
    # Вычисление площади
    print('\n' + '-' * 80)
    print('ШАГ 3: Вычисление площади фигуры методом Симпсона 3/8')
    print('-' * 80)
    x1, x2 = intersections[0], intersections[1]
    area, n = calculate_area(f, g, x1, x2, epsilon)
    
    # Вывод результатов
    print_results_table(intersections, area, n)
    
    # Визуализация
    visualize = input('Построить график? (y/n, по умолчанию y): ').strip().lower()
    if visualize != 'n':
        graph_visualize(f, g, intersections, area)
    
    print('\nПрограмма завершена успешно.')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n\nПрограмма прервана пользователем.')
    except Exception as e:
        print(f'\nОшибка: {e}')