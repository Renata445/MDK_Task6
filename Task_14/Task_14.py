# Последовательность Фибоначчи определяется так:
# φ0 = 0,  φ1 = 1,  φn = φn−1 + φn−2.
#По данному числу n определите n-е число Фибоначчи φn.
# Эту задачу можно решать и циклом for.

n=int(input())
a=0
b=1
k=1
if n==0:
    print(0)
elif n==1:
    print(1)
else:
    while k<n:
        t=b
        b=a+b
        a=t
        k+=1
    print(b)