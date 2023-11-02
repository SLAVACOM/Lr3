st = input("Введите строку заканчивающуюся точкой: ")

while st[-1] != ".":
    st = input("Cтрока не оканчивается точкой! Введите строку заканчивающуюся точкой: ")

st_lengh = len(st)
words = st.split()[:-1]
st_word_count = len(words)

min_word_lengh = len(min(words, key=len))
max_word_lengh = len(max(words, key=len))

norm_st = "".join(s * 2 for s in st if s != "*")

print(f"a) Длинна строки: {st_lengh}")
print(f"b) Количество слов в строке: {st_word_count}")
print(f"c) Длину самого короткого слова: {min_word_lengh}\n"
      f"   Длинна самого длинного слова: {max_word_lengh}")
print(f"d) Преобразованная строка: {norm_st}")
