import pandas as pd

df = pd.read_csv('C:/Users/User/Downloads/wild_boars.csv')
females = df[df['gender'] == 'Female']

print("Модальные значения по всем столбцам:")

with open('C:/Users/User/Downloads/mode_values.txt', 'w', encoding='utf-8') as f:
    f.write("Модальные значения по всем столбцам\n")
    
    for column in df.columns:
        if column == 'boar_id':
            continue
        
        if column == 'litter_size':
            data = females['litter_size'].dropna()
            column_name = f"{column} (только самки)"
        else:
            data = df[column]
            column_name = column
        
        mode_values = data.mode()
        if len(mode_values) == 0:
            mode_str = "нет моды"
        else:
            mode_str = mode_values.iloc[0]
        
        print(f"{column_name}: {mode_str}")
        f.write(f"{column_name}: {mode_str}\n")

print("\nРезультаты сохранены в файл: mode_values.txt")