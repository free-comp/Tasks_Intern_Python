#01. Вывести квадрат числа
# print('Введите число', end = ' ')
# numb = int (input())
# print ('Квадрат числа равен', numb**2)


# через метод:
def sq(x):
    return x ** 2

numb = int (input('Введите число: '))
print ('Квадрат числа равен', sq(numb))