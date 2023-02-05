# Определите количество четных элементов в последовательности, завершающейся числом 0.

element = -1
volume = -1
while element != 0:
    element = int(input("Введите число: "))
    if element % 2 == 0:
        volume += 1
print(volume)