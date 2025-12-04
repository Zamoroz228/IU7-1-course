'''
Иванов Андрей 
12 лаба
Сложение и деление и Наиболее часто встречающееся слово в каждом предложении
'''
from math import ceil
from re import finditer, IGNORECASE


def input_text() -> list[str]:
    # with open(file_path, mode='r', encoding='utf-8') as file:
    #     text = file.readlines()
    #     for i in range(len(text)):
    #         text[i] = text[i].strip()
    text = ['Один два три четыре 1 +2 /3',
            'один. Шесть, семь восемь девять один',
            'десять. Одинадцать, двенадцать',
            'Пять',
            'Одинадцать двенадцать. один',
            '1 три три три три. 1+3/0 1 +2',
            '3 52 + 52 /52.']
    return text


def output_text(text: list[str]) -> None:
    print('=' * 70)
    for string in text:
        print(string)
    print('=' * 70)
    return None

def menu() -> None:
    print('1. Выровнять текст по левому краю')
    print('2. Выровнять текст по правому краю')
    print('3. Выровнять текст по ширине')
    print('4. Удаление слова')
    print('5. Замена слова')
    print('6. Вычисление арифметических выражений + и /')
    print('7. Найти и удалить наиболее частое слово в предложениях')
    print('0. Выход')
    return None


def string_to_words(text: list[str]) -> list[list[str]]:
    words_text = []
    for i in text:
        words_text.append(i.split())
    return words_text


def delete_multy_spaces(text: list[str]) -> list[str]:
    new_text = []
    for i in text:
        new_text.append(i.strip())
    return replace_words(new_text, r' +',' ')


def longest_string(text: list[str]) -> int:
    return len(max(text, key = lambda x: len(x)))


def left_alignment(text: list[str]) -> list[str]:
    return delete_multy_spaces(text)


def right_alignment(text: list[str]) -> list[str]:
    text = delete_multy_spaces(text)
    max_len = longest_string(text)
    for i in range(len(text)):
        text[i] = ' ' * (max_len - len(text[i])) + text[i]
    return text


def middle_aligment(text: list[str]) -> list[str]:
    text = delete_multy_spaces(text)
    formatted_text = []
    words = string_to_words(text)
    max_len = longest_string(text)
    for i in range(len(text)):
        difference = max_len - len(text[i])
        if difference == 0:
            formatted_text.append(text[i])
        else:
            if (len(words[i]) - 1) == 0:
                formatted_text.append(text[i])
                continue
            added_spaces_number = ceil(difference / (len(words[i]) - 1))
            current_string = ''
            for word in words[i][:-1]:
                current_string += word + ' ' * min(difference + 1, added_spaces_number + 1)
                difference -= added_spaces_number
            current_string += words[i][-1]
            formatted_text.append(current_string)
    return formatted_text
            

def replace_words(text: list[str], old: str, new: str = '', register: bool = False) -> list[str]:
    for index, string in enumerate(text):
        if register:
            all_matches = finditer(old, string, IGNORECASE)
        else:
            all_matches = finditer(old, string)
        if all_matches:
            new_string = ''
            prev_end = 0
            for match in all_matches:
                new_string += string[prev_end : match.start()] + new
                prev_end = match.end()
            new_string += string[prev_end:]
            text[index] = new_string
    return text


def calculate(text: list[str]) -> list[str]:
    for index, string in enumerate(text):
        i = 0
        new_string = ''
        while i < len(string):
            if not string[i].isdigit():
                new_string += string[i]
                i += 1
                continue
            
            numbers = []
            operators = []
            begin_index = i
            
            while True:
                current_number = ''
                while i < len(string) and string[i].isdigit():
                    current_number += string[i]
                    i += 1
                if not current_number:
                    break
                numbers.append(int(current_number))
                end_index = i

                while i < len(string) and string[i] == ' ':
                    i += 1
                
                if i == len(string) or string[i] not  in '+/':
                    i = end_index
                    break
                
                operator = string[i]
                i += 1
                
                while i < len(string) and string[i] == ' ':
                    i += 1
                    
                if i == len(string) or not string[i].isdigit():
                    i = end_index
                    break
                
                operators.append(operator)
            if operators:
                operator_index = 0
                zero_division = False
                while operator_index < len(operators) and not zero_division:
                    operator = operators[operator_index]
                    if operator == '/':
                        if numbers[operator_index + 1] == 0:
                            zero_division = True
                            break
                        numbers[operator_index] = numbers[operator_index] / numbers.pop(operator_index + 1)
                        operators.pop(operator_index)
                    else:
                        operator_index += 1
                if zero_division:
                    new_string += string[begin_index:end_index]
                else:
                    new_string += str(sum(numbers))
            else:
                new_string += string[begin_index:end_index]
        text[index] = new_string
    return text


# def most_popular_word(text: list[str]) -> list[str]:
#     new_text = text
#     senteces = [[]]
#     senteces_pos = []
#     start_index = 0
#     punctuation_marks = '.,?!:;'
#     words = string_to_words(text)
#     for line_index, i in enumerate(words):
#         for word in i:
#             if word[-1] == '.':
#                 senteces[-1].append(word)
#                 senteces.append([])
#                 senteces_pos.append((start_index, line_index, text[line_index].find(word) + len(word)))
#                 start_index = line_index
#             else:
#                 senteces[-1].append(word)    
#     senteces = senteces[:-1]
#     for index, sentece in enumerate(senteces):
#         words = dict()
#         for word in sentece:
#             clear_word = word
#             for mark in punctuation_marks:
#                 clear_word = clear_word.replace(mark, '')
#             clear_word = clear_word.lower()
#             words[clear_word] = words.get(clear_word, 0) + 1
#         popular = max(words, key=words.get)
#         print('В предложении:', ' '.join(sentece), '\nУдалено слово:', popular)
#         prev_pos = 0
#         start, end, pos = senteces_pos[index]
#         new_text[start] = replace_words([text[start][prev_pos:]], popular, '', True)[0]
#         for i in range(start + 1, end):
#             new_text[i] = replace_words([text[i]], popular, '', True)[0]
#         new_text[end] = replace_words([text[end][:pos]], popular, '', True)[0] + text[end][pos:]
#         prev_pos = pos
#     return new_text


def most_popular_word(text: list[str]) -> list[str]:
    punctuation_marks = '.,?!:;'
    def clean_word(word: str) -> str:
        for i in punctuation_marks:
            word = word.replace(i, '')
        return word.lower()
    new_text = [''] * len(text)
    sentece = ''
    words = dict()
    start = 0
    prev_pos = 0
    for i in range(len(text)):
        for word in text[i].split():
            if word[-1] == '.':
                cln_word = clean_word(word)
                sentece += word + ' '
                words[cln_word] = words.get(cln_word, 0) + 1
                pos = text[i].find(word) + len(word)
                popular = max(words, key=words.get)
                print('В предложении:', sentece, '\nУдалено слово:', popular)
                new_text[start] += replace_words([text[start][prev_pos:]], popular, '', True)[0]
                for j in range(start + 1, i):
                    new_text[j] = replace_words([text[j]], popular, '', True)[0]
                new_text[i] = replace_words([text[i][:pos]], popular, '', True)[0]
                start = i
                prev_pos = pos
                words = dict()
                sentece = ''
            else:
                sentece += word + ' '
                cln_word = clean_word(word)
                words[cln_word] = words.get(cln_word, 0) + 1
    return new_text


def main():
    text = input_text()
    t = 0
    while True:
        if t % 3 == 0:
            menu()
        t += 1
        command = input('Введите номер команды: ')
        match command:
            case '1':
                text = left_alignment(text)
                output_text(text)
                
            case '2':
                text = right_alignment(text)
                output_text(text)
                
            case '3':
                text = middle_aligment(text)
                output_text(text)
                
            case '4':
                word = input('Введите слово для удаления: ')
                text = replace_words(text, word)
                output_text(text)
                
            case '5':
                old_word = input('Введите слово для замены: ')
                new_word = input('Введите слово на которое надо изменить: ')
                text = replace_words(text, old_word, new_word)
                output_text(text)
                
            case '6':
                text = calculate(text)
                output_text(text)
            case '7':
                text = most_popular_word(text)
                output_text(text)
            case '0':
                raise KeyboardInterrupt
            case _:
                print('Введите команду от 0 до 7')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nПрограма завершена!')
    except ZeroDivisionError:
        print('\nНельзя делить на 0!')