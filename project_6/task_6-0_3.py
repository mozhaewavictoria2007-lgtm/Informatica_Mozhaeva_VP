import pandas as pd
df = pd.read_csv('C:/Users/User/Downloads/wild_boars.csv')

median_values = df.median(numeric_only=True)

print("Медианные значения по всем столбцам:")
for column, value in median_values.items():
    print(f"{column}: {value:.2f}")

output_file = 'median_values.txt'

with open('C:/Users/User/Downloads/output_file3.txt', 'w', encoding='utf-8') as f:
    f.write("Медианные значения по всем столбцам\n")
    for column, value in median_values.items():
        f.write(f"{column}: {value:.2f}\n")

print(f"\nРезультаты сохранены в файл: {'C:/Users/User/Downloads/output_file3.txt'}")