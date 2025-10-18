'''
После каждого четного элемента целочисленного списка
добавить его удвоенное значение, без использования вложенных
циклов. Без insert append срезов
'''

list_with_numbers = list(map(int, input('Введите значения массива через пробел: ').split()))

amount_even_numbers = 0
for i in list_with_numbers:
    if i % 2 == 0:
        amount_even_numbers += 1

list_with_numbers += [None] * amount_even_numbers

write_index = len(list_with_numbers) - 1

for read_index in range(len(list_with_numbers) - amount_even_numbers - 1, -1, -1):
    
    if list_with_numbers[read_index] % 2 == 0:
        list_with_numbers[write_index] = list_with_numbers[read_index] * 2
        write_index -= 1
        
    list_with_numbers[write_index] = list_with_numbers[read_index]
    write_index -= 1
    read_index -= 1
    
print(list_with_numbers)