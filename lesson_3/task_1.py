num_dict = {'zero': 'ноль',
            'one': 'один ',
            'two': 'два',
            'three': 'три',
            'four': 'четыре',
            'five': 'пять ',
            'six': 'шесть',
            'seven': 'семь',
            'eight': 'восемь',
            'nine': 'девять',
            'ten': 'десять'}


def num_translate(my_num):
    '''Функция переводит числа от 0 до 10 c английского на русский язык !'''
    return num_dict.get(my_num)


print(num_translate(input('Ввидите число от 0 до 10 используя латиницу: ')))
