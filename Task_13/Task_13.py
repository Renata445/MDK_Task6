# Последовательность состоит из натуральных чисел и завершается числом 0. 
# Определите, сколько элементов этой последовательности равны ее наибольшему элементу.

max = 0
element = -1
k = 0
while element != 0:
    element = int(input("Введите число: "))
    if element > max:
        max, k = element, 1
    elif element == max:
        k += 1
print(k)