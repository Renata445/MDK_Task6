# Последовательность состоит из различных натуральных чисел и завершается числом 0. 
# Определите значение второго по величине элемента в этой последовательности. 
# Гарантируется, что в последовательности есть хотя бы два элемента.

max_1 = int(input("Введите число: "))
max_2 = int(input("Введите число: "))
if max_1 < max_2:
    max_1, max_2 = max_2, max_1
element = int(input("Введите число: "))
while element != 0:
    if element > max_1:
        max_2, max_1 = max_1, element
    elif element > max_2:
        max_2 = element
    element = int(input("Введите число: "))
print(max_2)