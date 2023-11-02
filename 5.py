import random

n, m = 24, 23

array = [[random.randint(-1100, 1000) for j in range(m)] for i in range(n)]
for i in range(n): print(*array[i])
max_number = max(array[i][j] for i in range(n) for j in range(m) if i + j % 2 == 1)

i_index = 0

for i in range(n):
    if max_number in array[i]:
        i_index = i

j_index = array[i_index].index(max_number)
print(f"Максимальное число: {max_number}\n"
      f"Его индексы ({i_index},{j_index})")
