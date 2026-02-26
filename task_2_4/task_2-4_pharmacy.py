main_num = int(input("Введите общее количество произведенных капсул: "))
size_pack = int(input("Введите количество капсул в одной упаковке: "))

full = main_num // size_pack
left_num = main_num % size_pack

print(f"--- Отчет фасовочного цеха ---")
print(f"Полных упаковок:\t{full}")
print(f"Остаток капсул:\t\t{left_num}")
