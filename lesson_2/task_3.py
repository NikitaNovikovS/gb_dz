list_staff_names = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in range(len(list_staff_names)):
    print(f'Привет, {list_staff_names[i].split()[-1].capitalize()}!')
