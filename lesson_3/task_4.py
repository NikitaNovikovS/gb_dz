def thesaurus_adv(*args):
    '''Функция принимает имена и фамилии сотрудников и возвращающую словарь
    в котором ключи — первые буквы имён,
    а значения — списки, содержащие имена'''
    names_dict = {}
    for name_surname in args:
        name, surname = name_surname.split()
        names_dict.setdefault(surname[0], {})
        names_dict[surname[0]].setdefault(name[0], [])
        names_dict[surname[0]][name[0]].append(name_surname)

    return names_dict


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
