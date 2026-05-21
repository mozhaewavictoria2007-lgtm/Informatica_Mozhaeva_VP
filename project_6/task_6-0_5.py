import pandas as pd

df = pd.read_csv('C:/Users/User/Downloads/wild_boars.csv')
females = df[df['gender'] == 'Female']

columns_info = {
    'age_years': ('years', False),
    'weight_kg': ('kg', False),
    'length_cm': ('cm', False),
    'shoulder_height_cm': ('cm', False),
    'tusk_length_cm': ('cm', False),
    'litter_size': ('piglets', True),
    'health_score': ('points', False),
    'territory_ha': ('ha', False)
}

p_values = [0.25, 0.50, 0.75, 0.90, 0.95, 1.00]
p_names = ['Percentile 25 (Q1)', 'Median 50 (Q2)', 'Percentile 75 (Q3)', 
           'Percentile 90', 'Percentile 95', 'Max']

print("ПЕРЦЕНТИЛИ ПО ВСЕМ СТОЛБЦАМ")

with open('C:/Users/User/Downloads/percentiles.txt', 'w', encoding='utf-8') as f:
    f.write("ПЕРЦЕНТИЛИ ПО ВСЕМ СТОЛБЦАМ\n")
    
    for column, (unit, use_females) in columns_info.items():
        if use_females:
            data = females[column].dropna()
            col_name = f"{column} (только самки)"
        else:
            data = df[column].dropna()
            col_name = column
        
        print(f"\n{col_name}:")
        f.write(f"{col_name}:\n")
        
        for p, name in zip(p_values, p_names):
            value = data.quantile(p)
            print(f"  {name}: {value:.1f} {unit}")
            f.write(f"  {name}: {value:.1f} {unit}\n")
        
        f.write("\n")

print("Результаты сохранены в 'percentiles.txt'")