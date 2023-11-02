number = int(input("Введите число: "))
numbers = [None] * 2 + [i + 1 for i in range(1, number)]
numbers_7 = [1] + [i for i in range(7, number, 7)]
def prost(x):
    return all(x % i for i in range(2, int(x ** 0.5) + 1))


i = 2
while i * i < number:
    if numbers[i] is not None:
        for i in range(i * i, number + 1, i):
            numbers[i] = None
    i += 1
prost_numbers = ([numbers[i] for i in range(number) if numbers[i] is not None])
print(f"а) Все числа от 1 до {number}, кратные 7:", *numbers_7)
print(f'б) Все простые числа от 1 до {number}:', *prost_numbers)
