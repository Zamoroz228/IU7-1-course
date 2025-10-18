'''
Удалить все положительные элементы целочисленного списка за один цикл. Без del pop remove срезов
'''

list_with_numbers = list(map(int, input('Введите значения массива через пробел: ').split()))
begin_len_list = len(list_with_numbers)

current_write_index = 0

for i in range(begin_len_list):
    if list_with_numbers[i] <= 0:
        list_with_numbers[current_write_index] = list_with_numbers[i]
        current_write_index += 1

list_with_numbers = list_with_numbers[:current_write_index]

print(list_with_numbers)