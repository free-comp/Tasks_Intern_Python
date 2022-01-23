# 12. Удалить вторую цифру трёхзначного числа

def del_second(x):
    one_digit = (numb - numb%100)//100
    third_digit = numb%10
    return one_digit*10 + third_digit

numb = int(input ('Введите трехзначное число: '))
if (numb < 0):
    numb = abs(numb)
    rezult = -int(del_second(numb))
else:
    rezult = del_second(numb)
print('Удаление второй цифры введенного числа даст результат: ', rezult)