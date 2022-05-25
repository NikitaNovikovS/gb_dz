for i in range(101):
    if i % 10 == 1 and i != 11:
        print(i, 'процент')
    elif 5 <= i <= 20 or 5 <= i % 10 <= 9 or i == 100:
        print(i, 'процентов')
    elif 2 <= i % 10 <= 4:
        print(i, 'процента')
