import random

def random_int(): return random.randint(-1_000_000,1_000_000)

element_count = int(input("Введите количество слов для генераци: "))
elements = [random_int() for i in range(element_count)]
print( elements)
min_number_index = elements.index(min(elements))
print( min_number_index)
min_number_index += min_number_index%2
result = [elem for i, elem in enumerate(elements) if (elem <= 0) or (i <= min_number_index) or (i % 2 != 0)]
