list_cubes = [_ ** 3 for _ in range(1, 1001, 2)]
sum_of_cubes = 0

for i in list_cubes:
    i += 17
    result = list(map(int, str(i)))
    if sum(result) % 7 == 0:
        sum_of_cubes += i

print(sum_of_cubes)
