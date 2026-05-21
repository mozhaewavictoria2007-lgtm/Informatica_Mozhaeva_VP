import pandas as pd
df = pd.read_csv('C:/Users/User/Downloads/wild_boars.csv')

mean_values = df.mean(numeric_only=True)  

print("Средние значения по всем столбцам:")
for column, value in mean_values.items():
    print(f"{column}: {value:.2f}")

output_file = 'mean_values.txt'

with open('C:/Users/User/Downloads/output_file2.txt', 'w', encoding='utf-8') as f:
    f.write("Средние значения по всем столбцам\n")
    for column, value in mean_values.items():
        f.write(f"{column}: {value:.2f}\n")

print(f"\nРезультаты сохранены в файл: {'C:/Users/User/Downloads/output_file2.txt'}")