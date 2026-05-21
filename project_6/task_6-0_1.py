import pandas as pd
df = pd.read_csv('C:/Users/User/Downloads/wild_boars.csv')
pd.set_option('display.max_rows', None)

print("Столбец 'tusk_length_cm':")
print(df['tusk_length_cm'])

min_tusk = df['tusk_length_cm'].min()
print(f"Самый короткий клык: {min_tusk} см")

max_tusk = df['tusk_length_cm'].max()
print(f"Самый длинный клык: {max_tusk} см")