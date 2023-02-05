# Определите среднее значение всех элементов последовательности, завершающейся числом 0.

element = int(input("Введите число: "))
sum = 0
size = 0
while element != 0:
    sum += element
    size += 1
    element = int(input("Введите число: "))
print(sum / size)