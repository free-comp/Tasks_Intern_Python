#07 Показать числа от -N до N.

def output(n):
    for i in range(-n,n+1):
        print(i, end = ' ')
    print()
        
numb = int(input('Введите число: '))
print (f'Отрезок от {-numb} до {numb}:')
output(abs(numb))