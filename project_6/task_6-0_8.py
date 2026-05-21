import pandas as pd

df = pd.read_csv('C:/Users/User/Downloads/wild_boars.csv')

males = df[df['gender'] == 'Male']['tusk_length_cm'].dropna()
females = df[df['gender'] == 'Female']['tusk_length_cm'].dropna()

males_cv = (males.std() / males.mean()) * 100
females_cv = (females.std() / females.mean()) * 100

print("Коэффициент вариации длины клыков:")
print(f"  Самцы: {males_cv:.2f}%")
print(f"  Самки: {females_cv:.2f}%")

with open('C:/Users/User/Downloads/tusk_cv.txt', 'w', encoding='utf-8') as f:
    f.write(f"Male: {males_cv:.2f}%\n")
    f.write(f"Female: {females_cv:.2f}%\n")

print("\nРезультаты сохранены в 'tusk_cv.txt'")