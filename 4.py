number = int(input("Введите число: "))
numbers = [None]*2+[i+1 for i in range(1,number)]
prost_number = []

numbers_7 = [1] + [i for i in range(7, number, 7)]

for i in range(2,int(number**0.5)+1):
    if number%i == 0:
        prost_number.append(i)
        if number/i != i : prost_number.append(int(number/i))

print(f"а) Все числа от 1 до n, кратные 7:",numbers_7)