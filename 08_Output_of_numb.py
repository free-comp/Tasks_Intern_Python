# 08 Показать четные числа от 1 до N

def output(n):
    if (n > 0):
        for i in range(1, n+1):
            if (i % 2 == 0):
                print(i, end=' ')
        print()
    # необязательно (если ввести отрицательное число):
    elif (n < 0):
        for i in range(0, n-1, -2):
            if (i % 2 == 0):
                print(i, end=' ')
        print()
    else:
        print(0)


numb = int(input('Введите число: '))
print(f'Четные числа на отрезке от 1 до {numb}:')
output(numb)
 
