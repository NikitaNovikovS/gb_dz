def thesaurus(*args):
    '''Функция принимает имена сотрудников и возвращающую словарь
    в котором ключи — первые буквы имён,
    а значения — списки, содержащие имена'''
    names_dict = {}
    for name in args:
        first_char = name[0]
        if names_dict.get(first_char):
            names_dict[first_char].append(name)
        else:
            names_dict.setdefault(first_char, [name])
    return names_dict


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
