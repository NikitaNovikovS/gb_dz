from random import uniform

my_prices = [round(uniform(10, 500), 2) for _ in range(20)]
for i in my_prices:
    i = str(i).split('.')
    print(f'{i[0]} руб {i[1].ljust(2, "0")} коп,', end=' ')

print()
print('Список до сортировки                   :', id(my_prices), sorted(my_prices))
print('Список после сортировки по возрастанию :', id(my_prices), my_prices)
print('Список после сортировки по убыванию    :', id(my_prices), my_prices[::-1])
print('Пять товаров с смаой высокой ценой     :', id(my_prices), my_prices[::-1][:5])
