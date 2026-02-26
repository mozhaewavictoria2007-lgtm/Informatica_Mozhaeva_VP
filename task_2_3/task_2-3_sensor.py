fio = input("Введите ФИО оператора: ")
info = input("Введите текущее значение давления (Па): ")

with open("C:/Users/User/Desktop/sensor_log.txt", "a", encoding="utf-8") as report:
     report.write(f"{fio}:\t{info} Па\n")
print("Данные успешно сохранены в sensor_log.txt")
