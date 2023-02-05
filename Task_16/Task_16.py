# Дана последовательность натуральных чисел, завершающаяся числом 0. 
# Определите, какое наибольшее число подряд идущих элементов этой последовательности равны друг другу.

prev = -1
curr_rep_len = 0
max_rep_len = 0
element = int(input("Введите число: "))
while element != 0:
    if prev == element:
        curr_rep_len += 1
    else:
        prev = element
        max_rep_len = max(max_rep_len, curr_rep_len)
        curr_rep_len = 1
    element = int(input("Введите чило: "))
max_rep_len = max(max_rep_len, curr_rep_len)
print(max_rep_len)