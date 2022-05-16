duration = int(input())

sec = duration % 60
minutes = duration % 3600 // 60
hour = duration % 86400 // 3600
day = duration // 86400

if duration < 60:
    print(f'{sec} сек')
elif duration < 3600:
    print(f'{minutes} мин {sec} сек')
elif duration < 86400:
    print(f'{hour} час {minutes} мин {sec} сек')
elif duration > 86400:
    print(f'{day} дн {hour} час {minutes} мин {sec} сек')
