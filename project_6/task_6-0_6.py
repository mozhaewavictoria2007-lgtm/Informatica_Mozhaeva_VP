import pandas as pd

df = pd.read_csv('C:/Users/User/Downloads/wild_boars.csv')

males = df[df['gender'] == 'Male']
females = df[df['gender'] == 'Female']

males_q1 = males['length_cm'].quantile(0.25)
males_q3 = males['length_cm'].quantile(0.75)
males_iqr = males_q3 - males_q1

females_q1 = females['length_cm'].quantile(0.25)
females_q3 = females['length_cm'].quantile(0.75)
females_iqr = females_q3 - females_q1

print("IQR по длине тела (length_cm):")
print(f"Самцы: Q1={males_q1:.1f} см, Q3={males_q3:.1f} см, IQR={males_iqr:.1f} см")
print(f"Самки: Q1={females_q1:.1f} см, Q3={females_q3:.1f} см, IQR={females_iqr:.1f} см")

with open('C:/Users/User/Downloads/iqr_length.txt', 'w', encoding='utf-8') as f:
    f.write(f"Male: {males_iqr:.1f} cm\n")
    f.write(f"Female: {females_iqr:.1f} cm\n")

print("\nРезультаты сохранены в 'iqr_length.txt'")