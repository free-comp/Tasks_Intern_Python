# 12. Удалить вторую цифру трёхзначного числа

def del_second(x):
    one_digit = str((numb - numb%100)//100)
    third_digit = str(numb%10)
    return one_digit + third_digit

numb = int(input ('Введите трехзначное число: '))
if (numb < 0):
    numb = abs(numb)
    rezult = -int(del_second(numb))
    print('Удаление второй цифры введенного числа даст результат: ', rezult)
else:
    print ('Удаление второй цифры введенного числа даст результат: ', del_second(numb))