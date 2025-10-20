'''дан массив строк удалить только гласные один цикл'''

list_with_strings = []
glasn_chars = 'AEIOUYaeiouy'

while True:
    
    current_string = input()
    
    if current_string == '':
        break
    
    list_with_strings.append(current_string)
    
for i in range(len(list_with_strings)):
        
    new_s = ''    
    for char in list_with_strings[i]:
        if char not in glasn_chars:
            new_s += char
    
    list_with_strings[i] = new_s 
    #-----------------------
    # for char in glasn_chars:
    #     list_with_strings[i] = list_with_strings[i].replace(char, '')
    #-----------------------
    # list_with_strings[i] = list_with_strings[i].replace('A', '').replace('a', '')
    # list_with_strings[i] = list_with_strings[i].replace('E', '').replace('e', '')
    # list_with_strings[i] = list_with_strings[i].replace('I', '').replace('i', '')
    # list_with_strings[i] = list_with_strings[i].replace('O', '').replace('o', '')
    # list_with_strings[i] = list_with_strings[i].replace('U', '').replace('u', '')
    # list_with_strings[i] = list_with_strings[i].replace('Y', '').replace('y', '')
    
print('-' * 44)
[print(i) for i in list_with_strings]