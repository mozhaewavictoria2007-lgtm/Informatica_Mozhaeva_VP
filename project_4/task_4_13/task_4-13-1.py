print("Введите 4 числа по очереди:")

a = float(input("Введите первое число:")) 
b = float(input("Введите второе число:")) 
c = float(input("Введите третье число:")) 
d = float(input("Введите четвертое число:")) 

if a < b:
    min_value = a
else: 
    min_value = b

if c < d :
    min_value1 = c
else: 
    min_value1 = d

if min_value < min_value1:
    print("Минимальное из четырех чисел:", min_value)
else:
    print("Минимальное из четырех чисел:", min_value1)
