# 04. Найти максимальное из трех чисел

def max (numb_1, numb_2, numb_3):
    result = numb_1
    if (numb_2 > result): result = numb_2
    if (numb_3 > result): result = numb_3
    return result

print ('Введите три числа: ')
first_numb = int(input())
second_numb = int(input())
third_numb = int(input())

maximum = max (first_numb, second_numb, third_numb)
print ('Максимальное число:', maximum)


