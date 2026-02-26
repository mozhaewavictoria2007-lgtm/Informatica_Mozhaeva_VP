print("=== Анализ последовательности ДНК ===\n")

dna = input("Введите последовательность ДНК: ").upper()
print(f"\nПоследовательность в верхнем регистре: {dna}")
print("\nПодсчёт нуклеотидов:\n")
dna_len = len(dna)

print("A:", dna.count("A"))
print("T:", dna.count("T"))
print("G:", dna.count("G"))
print("C:", dna.count("C"))

print("\nОбщая длина:", dna_len, "нуклеотидов")
