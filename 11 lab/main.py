'''
Иванов Андрей
Иу7-16Б
Лаба 11
'''
from sys import exit
from string import digits
from typing import Callable

EPS = 1e-8


def f(x: float) -> float:
    y = x ** 2
    return y


def F(x: float) -> float:
    y = 1/3 * x ** 3
    return y


def left_rectangle(f: Callable, begin: float, end: float, n: int) -> float:
    if begin > end:
        return -left_rectangle(f, end, begin, n)
    
    h = (end - begin) / n
    integral = 0
    
    for i in range(n):
        integral += f(begin + h * i) * h
        
    return integral


def simpson_3_8(f: Callable, begin: float, end: float, n: int) -> float:
    if begin > end:
        return -simpson_3_8(f, end, begin, n)
    
    if n % 3 != 0:
        raise ValueError
    
    h = (end - begin) / n
    integral = f(begin) + f(end)

    for i in range(1, n):
        x_i = begin + i * h
        if i % 3 == 0:
            integral += 2 * f(x_i)
        else:
            integral += 3 * f(x_i)

    integral = (3 * h / 8) * integral
    return integral


def integral(F: Callable, begin: float, end: float) -> float:
    result = F(end) - F(begin)
    return result


def float_input(dirty_number: str) -> float:
    number = dirty_number.strip()
    is_float = False
    is_negative = False 
    current_number = ''
    
    for char in number:
        if char == '-' and not current_number:
            is_negative = not is_negative
        elif char == '-' and current_number[-1] == 'e':
            current_number += '-'
        elif char == '.' and current_number and not is_float:
            is_float = True
            current_number += '.'
        elif char == '.' and is_float:
            exit('Ошибка: Неправильно введено!')
        elif char == 'e' or char == 'E':
            current_number += 'e'
        elif char in digits:
            current_number += char
        else:
            exit('Ошибка: Введен символ отличный от цифр!')
    
    if not current_number:
        exit('Ошибка: Число полностью состоит из минусов!')
    
    float_number = float('-' * is_negative + current_number)
    return float_number


def integral_table(simpson: list[str], rect: list[str], sizes: list[int]) -> None:
    n = 76
    table = '-' * n + '\n'
    table += f'|{'M\\N':^30}|{sizes[0]:^21.7g}|{sizes[1]:^21.7g}|\n{'-' * n}\n'
    
    table += f'|{'Метод Симпсона':^30}|'
    for i in simpson:
        table += f'{i:^21}|'
    table += f'\n{'-' * n}\n'
    
    table += f'|{'Метод левых прямоугольников':^30}|'
    for i in rect:
        table += f'{i:^21}|'
    table += f'\n{'-' * n}\n'
    print(table)


def error_table(errors: list[tuple], real: float) -> None:
    hatch = 95
    table = '-' * hatch + '\n'
    table += f'|{'Метод':^30}|{'N':^10}|{'Значение':^15}|{'Абс. погрешность':^16}|{'Отн. погрешность %':^18}|\n{'-' * hatch}\n'
    
    for method_name, n, value in errors:
        abs_error = abs(value - real)
        if abs(real) > EPS:
            rel_error = abs_error / abs(real) * 100
        else:
            rel_error = float('inf')
        table += f'|{method_name:^30}|{n:^10.6g}|{value:^15.7g}|{abs_error:^16.7g}|{rel_error:^18.7g}|\n{'-' * hatch}\n'
        
    print(table)


def find_accuracy(method: Callable, f:Callable,
                    begin: float, end: float, begin_n: int, step_n: int,
                    epsilon: float) -> tuple:
    n = begin_n
    
    while True:
        i_n = method(f, begin, end, n)
        i_2n = method(f, begin, end, 2 * n)
        
        if abs(i_n - i_2n) < epsilon:
            return i_n, n
        
        n += step_n


def test_algotitms(f: Callable, F: Callable, begin: float, end: float,
                    n1: int, n2: int, epsilon: float) -> None:
    simpson_printable = []
    rectangle_printable = []
    simpson_results = []
    rectangle_results = []
    errors_data = []
    for size in (n1, n2):
        if size % 3 != 0:
            simpson_printable.append('-')
        else:
            i_simpson = simpson_3_8(f, begin, end, size)
            simpson_printable.append(f'{i_simpson:.7g}')
            simpson_results.append((size, i_simpson))
            errors_data.append(('Метод Симпсона 3/8', size, i_simpson))
        
        i_rect = left_rectangle(f, begin, end, size)
        rectangle_printable.append(f'{i_rect:.7g}')
        rectangle_results.append((size, i_rect))
        errors_data.append(('Метод левых прямоугольников', size, i_rect))
        
    print('Таблица с вычислениями:')
    integral_table(simpson_printable, rectangle_printable, [n1, n2])

    print('Таблица погрешностей:')
    real_integral = integral(F, begin, end)
    error_table(errors_data, real_integral)
    print(f'Точное значение интеграла: {real_integral:.10g}\n')
    
    best_method = min(errors_data, key=lambda x: abs(x[2] - real_integral))
    print(f'Наиболее точный метод: {best_method[0]} при N={best_method[1]}\n'
          f'Значение: {best_method[2]:.10g}\n'
          f'Абсолютная погрешность: {abs(best_method[2] - real_integral):.10g}\n')
    
    if best_method[0] == 'Метод Симпсона 3/8':
        less_method = left_rectangle
        method_name = 'метода левых прямоугольников'
        begin_n = 1
        step_n = 1
    else:
        less_method = simpson_3_8
        method_name = 'метода Симпсона 3/8'
        begin_n = 3
        step_n = 3
    
    result, n = find_accuracy(less_method, f, begin, end, begin_n, step_n, epsilon)
    
    print(f'Поиск N для {method_name} с точностью E = {epsilon}:')
    
    print(f'Найденное N: {n}\n'
            f'Приближенное значение интеграла: {result:.10g}\n'
            f'Абсолютная погрешность относительно точного: {abs(result - real_integral):.10g}')

if __name__ == '__main__':
    begin, end, *_ = map(float_input, input('Введите начало и конец интегрирования: ').split())
    n1, n2, *_ = map(float_input,input('Введите n1 и n2: ').split())
    if n1.is_integer() and n2.is_integer():
        n1, n2 = int(n1), int(n2)
    else:
        exit('Ошибка: числа n1 и n2 должны быть целочисленными!')
    if n1 <= 0 or n2 <= 0:
        exit('Ошибка: n1 и n2 должны быть положительны!')
        
    epsilon_input = input(f'Введите точность E (по умолчанию {EPS}): ').strip()
    epsilon = float_input(epsilon_input) if epsilon_input else EPS
    
    if epsilon <= 0:
        exit('Ошибка: точность должна быть положительной!')
    
    test_algotitms(f, F, begin, end, n1, n2, epsilon)