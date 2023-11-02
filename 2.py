import random

def random_int(): return random.randint(-1_000_000, 1_000_000)

element_count = int(input("Введите кол-во чисел: "))
elements = [random_int() for i in range(element_count)]
print(*elements)
negative = []
negative_index = []
pos = 0

while (pos < element_count):
    if elements[pos] < 0:
        left = pos
        while (pos < element_count and elements[pos] < 0):
            pos += 1
        else:
            negative.append(pos - left)
            negative_index.append([left, pos])
    pos += 1
maxx = negative_index[negative.index(max(negative))]
print("Результат:", *elements[:maxx[0]] + elements[maxx[1]:] + elements[maxx[0]:maxx[1]])
