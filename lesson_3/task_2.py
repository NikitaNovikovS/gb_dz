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


def num_translate_adv(my_num):
    if my_num[0].isupper():
        '''Функция переводит числа от 0 до 10 c английского на русский язык со *!'''
        return num_dict.get(my_num.lower()).capitalize()
    else:
        return num_dict.get(my_num)


print(num_translate_adv(input('Ввидите число от 0 до 10 используя латиницу: ')))
