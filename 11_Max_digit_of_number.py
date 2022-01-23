# 11 Дано число из отрезка [10, 99]. Показать наибольшую цифру числа

def max_dig(numb):
    dig_one = numb % 10
    dig_second = numb // 10
    if ( dig_one > dig_second):
        return  dig_one
    elif (dig_second >  dig_one):
        return dig_second
    else:
        return dig_second
    
    
import random
numb = random.randint(10, 99)
print ('Дано число из отрезка [10, 99]:', numb)
print ('Наибольшая цифра числа:', max_dig(numb))
