array = input("Введите числа через запятую:").split(', ')
sum = 0

for i in range(len(array)):
    if i % 2 != 0:
        sum += int(array[i])

print("Сумма элементов с нечетными индексами:", sum)
