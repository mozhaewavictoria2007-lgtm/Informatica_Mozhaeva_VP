import pandas as pd

df = pd.read_csv('C:/Users/User/Downloads/wild_boars.csv')
females = df[df['gender'] == 'Female']

columns = {
    'age_years': 'years',
    'weight_kg': 'kg',
    'length_cm': 'cm',
    'shoulder_height_cm': 'cm',
    'tusk_length_cm': 'cm',
    'litter_size': 'piglets (только самки)',
    'health_score': 'points',
    'territory_ha': 'ha'
}

print("ДИСПЕРСИЯ, СТАНДАРТНОЕ ОТКЛОНЕНИЕ, КОЭФФИЦИЕНТ ВАРИАЦИИ")
print(f"{'Параметр':<25} {'Дисперсия':<15} {'Ст. отклонение':<18} {'CV (%)':<10}")

results = []

for col, unit in columns.items():
    if col == 'litter_size':
        data = females[col].dropna()
        col_display = col
    else:
        data = df[col].dropna()
        col_display = col
    
    variance = data.var()
    std_dev = data.std()
    mean_val = data.mean()
    cv = (std_dev / mean_val) * 100
    
    results.append({
        'column': col_display,
        'variance': variance,
        'std': std_dev,
        'cv': cv,
        'unit': unit
    })
    
    print(f"{col_display:<25} {variance:<15.2f} {std_dev:<18.2f} {cv:<10.2f}")

with open('C:/Users/User/Downloads/variability_stats.txt', 'w', encoding='utf-8') as f:
    f.write("ДИСПЕРСИЯ, СТАНДАРТНОЕ ОТКЛОНЕНИЕ И КОЭФФИЦИЕНТ ВАРИАЦИИ\n")

    for r in results:
        f.write(f"{r['column']} [{r['unit']}]:\n")
        f.write(f"  Дисперсия: {r['variance']:.2f}\n")
        f.write(f"  Стандартное отклонение: {r['std']:.2f}\n")
        f.write(f"  Коэффициент вариации: {r['cv']:.2f}%\n\n")

print(f"\nРезультаты сохранены в 'variability_stats.txt'")