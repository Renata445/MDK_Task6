# Дано натуральное число A. Определите, каким по счету числом Фибоначчи оно является, 
# то есть выведите такое число n, что φn = A. 
# Если А не является числом Фибоначчи, выведите число -1

a = int(input("Введите число: "))
if a == 0:
    print(0)
else:
    prew, next = 0, 1
    n = 1
    while next <= a:
        if next == a:
            print(n)
            break
        prew, next = next, prew + next
        n += 1
    else:
        print(-1)