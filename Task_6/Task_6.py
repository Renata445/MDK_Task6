# Определите сумму всех элементов последовательности, завершающейся числом 0. 
# В этой и во всех следующих задачах числа, следующие за первым нулем, учитывать не нужно.

sum = 0
element = int(input("Введите число: "))
while element != 0:
    sum += element
    element = int(input("Введите числа: "))
print(sum)