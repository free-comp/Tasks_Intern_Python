# 13. Выяснить, кратно ли число заданному, если нет, вывести остаток.

def divis(numb, div):
    if (numb % div == 0):
        return print ('Делитель кратен заданному числу')
    else:
        ost = numb % div
        return print ('Остаток от деления:', ost)


numb = int(input('Введите число: '))
div = int(input('Введите делитель для данного числа: '))
divis(numb, div)