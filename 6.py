import random

x,y,z = 3,5,7

array = [[[random.randint(-1100, 1000) for zz in range(z)] for yy in range(y)] for xx in range(x)]
rez = x_index = y_index = z_index = 0
for i in range(x):
    for j in range(y):
        print(*array[i][j])
        mmax = max(array[i][j])
        if rez<mmax:
            x_index = i
            y_index = j
            z_index = array[i][j].index(mmax)
            rez = mmax
    print("="*6**2)
print(f"Максимальный элемент: {rez}\n"
      f"Его индексы: ({x_index},{y_index},{z_index})")