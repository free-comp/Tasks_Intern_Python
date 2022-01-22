# 02. Даны два числа. Показать большее и меньшее число

def max (arg_1, arg_2):
    result = arg_1
    if (arg_2 > result): result = arg_2
    return result

def min (arg_1, arg_2):
    result = arg_1
    if (arg_2 < result): result = arg_2
    return result

print ('Введите первое число', end = ' ')
first_number = int (input())
print ('Введите второе число', end = ' ')
second_number = int (input())
if (first_number == second_number):
    print ('Числа равны')
else:
    Max = max (first_number,second_number)
    Min = min (first_number,second_number)
    print (f'Наибольшее: {Max}, наименьшее: {Min}')


# Второй способ:
# if (first_number > second_number):
#     print('Большее число: ', first_number)
#     print('Меньшее число: ', second_number)
# elif (first_number == second_number):
#     print('Числа равны')
# else:
#     print('Большее число: ', second_number)
#     print('Меньшее число: ', first_number)
