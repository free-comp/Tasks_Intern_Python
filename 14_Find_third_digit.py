# 14. Найти третью цифру числа или сообщить, что её нет.

def find(number):
    number = abs (number) # на случай ввода отрицательного числа
    third_dig = (number % 1000 - (number % 1000) % 10)//100
    return third_dig


numb = int(input('Введите число: '))
if (abs(numb) < 100):
    print('Третьей цифры в данном числе нет')
else:
    print('Третья цифра в данном числе: ', find(numb))




# поиск с левой стороны (какая-то ерунда):
# numb = (input('Введите число: '))
# if (int (numb) > 0):
#     if (len(numb) < 3):
#         print ('Третьей цифры нет')
#     else:
#         print(numb[2])
# else:
#     if (len(numb) < 4):
#         print ('Третьей цифры нет')
#     else:
#         print(numb[3])

