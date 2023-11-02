import random

def random_int(): return random.randint(-1_000_000,1_000_000)

# element_count = int(input("Введите количество слов для генераци: "))
element_count = 10
elements = [random_int() for i in range(element_count)]
print(*elements)

start_index = end_index = max_start_index = max_end_index = None
for i in range(element_count):
    if elements[i] < 0 and start_index is None:
        start_index = i
        end_index = i
    elif elements[i] < 0 and start_index is not None:
        end_index+=1
    elif elements[i]>= 0 and start_index is not None:
        if max_start_index is None or (end_index - start_index) > (max_end_index-max_start_index):
            max_start_index = start_index
            max_end_index = end_index
            start_index = None
            end_index = None

if max_start_index is not None and max_end_index is not None:
    print(*elements[:max_start_index]+elements[max_end_index+1:]+elements[max_start_index:max_end_index+1])
    print(elements[max_start_index:max_end_index+1])
else:print(*elements)