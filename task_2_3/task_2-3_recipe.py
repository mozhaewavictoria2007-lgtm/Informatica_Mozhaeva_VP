envir = input("Введите название питательной среды: ")
conc = input("Введите концентрацию агара (%): ")
temp = input("Введите температуру стерилизации (°C): ")

with open("C:/Users/User/Desktop/recipe.txt", "w", encoding="utf-8") as report:
    report.write(f"\t{envir}\n")
    report.write(f"Концентрация:\t{conc}%\n")
    report.write(f"Температура:\t{temp}°C")

print("Файл 'recipe.txt' успешно сформирован!")
