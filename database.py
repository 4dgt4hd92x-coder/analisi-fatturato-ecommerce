import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt
import seaborn as sns

url = 'https://api.open-meteo.com/v1/forecast?latitude=52.374&longitude=4.8897&hourly=temperature_2m'
r = requests.get(url)

print(r.json())

#Calcolare le ore di sole
def calculate_sun_hours(temperature_data):
    sun_hours = 0
    for temp in temperature_data:
        if temp > 20:  # Consideriamo sole se la temperatura è superiore a 20°C
            sun_hours += 1
    return sun_hours

print(calculate_sun_hours(r.json()['hourly']['temperature_2m']))

# Calcolare la media delle temperature
def calculate_average_temperature(temperature_data):
    return np.mean(temperature_data)

print(calculate_average_temperature(r.json()['hourly']['temperature_2m']))

# Creare un DataFrame con i dati
data = {
    'hour': r.json()['hourly']['time'],
    'temperature': r.json()['hourly']['temperature_2m']
}   
df = pd.DataFrame(data)
# Converti la colonna hour in oggetti datetime
df['hour'] = pd.to_datetime(df['hour'])

# Estrai l'ora (0-23) e il giorno della settimana
df['ora_del_giorno'] = df['hour'].dt.hour
df['giorno'] = df['hour'].dt.day_name()

# Visualizzare la distribuzione delle temperature
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='ora_del_giorno', y='temperature', marker='o', color='orange')

plt.title('Andamento Orario della Temperatura ad Amsterdam', fontsize=15)
plt.xlabel('Ora del Giorno (0-23)', fontsize=12)
plt.ylabel('Temperatura (°C)', fontsize=12)
plt.xticks(range(0, 24)) # Mostra ogni singola ora sull'asse X
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

fasce_calde = df.groupby('ora_del_giorno')['temperature'].mean().sort_values(ascending=False)

print("Le 3 fasce orarie mediamente più calde sono:")
print(fasce_calde.head(3).sort_values(ascending=False))