# 05. Написать программу вычисления значения функции y = f(x).

import math

def f(x):
    return math.sin(x)


print('Введите значение х:', end = ' ')
x = int (input())

print (f'f(x) = sin({x}) =', f(x))

