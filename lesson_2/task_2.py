my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for x in range(len(my_list)):
    if my_list[x].isdigit():
        my_list[x] = f'"{my_list[x].rjust(2, "0")}"'
    if my_list[x].find('+') == 0:
        my_list[x] = f'"{my_list[x].zfill(3)}"'
print(*my_list)


