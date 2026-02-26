weight = float(input("Введите вес (кг): "))
height = float(input("Введите рост (см): "))

bmi = (weight) / ((height/100) ** 2)
print(f"--- Отчет о состоянии здоровья ---")
print(f"Рост:\t {height}")
print(f"Масса:\t{weight}")
print(f"Индекс массы тела пациента: \t{bmi:.2f}")
