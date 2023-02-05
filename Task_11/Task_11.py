# Последовательность состоит из натуральных чисел и завершается числом 0. 
# Определите, сколько элементов этой последовательности больше предыдущего элемента.

element = int(input("Введите число: "))
answer = 0
while element != 0:
    next_element = int(input("Введите число: "))
    if next_element != 0 and element < next_element:
        answer += 1
    element = next_element
print(answer)