import pandas as pd
import numpy as np
import matplotlib as mp

iris = pd.read_csv('dati.csv')

print (iris)

def somma_fatturato_netto(df):
    # 1. Pulizia del doppio punto: trasformiamo in stringa e prendiamo solo i primi 
    # caratteri utili prima del secondo punto. 
    # Esempio: '450.00.00' diventa '450.00'
    def pulisci_doppio_punto(valore):
        valore = str(valore).strip()
        parti = valore.split('.')
        if len(parti) > 2:
            # Ricostruisce prendendo solo la parte intera e i primi decimali
            return parti[0] + '.' + parti[1]
        return valore

    # Applichiamo la pulizia specifica
    importo_pulito = df['Importo'].apply(pulisci_doppio_punto)
    
    # 2. Ora la conversione funzionerà!
    importo_float = pd.to_numeric(importo_pulito, errors='coerce').fillna(0)
    
    # 3. Filtro per status
    maschera = df['Status_Ordine'].str.strip() == 'Completato'
    
    return (importo_float * maschera).sum()

print("La somma FINALMENTE corretta è:", somma_fatturato_netto(iris))


#Faccio un grafico a barre per visualizzare il fatturato netto per ogni categoria di prodotto
import matplotlib.pyplot as plt

# Raggruppiamo per categoria di prodotto e sommiamo il fatturato netto
fatturato_per_categoria = iris.groupby('Categoria_Prodotto')['Importo'].apply(lambda x: somma_fatturato_netto(iris[iris['Categoria_Prodotto'] == x.name]))

# Creiamo il grafico a barre
plt.figure(figsize=(10, 6))
fatturato_per_categoria.plot(kind='bar', color='skyblue')
plt.title('Fatturato Netto per Categoria di Prodotto')
plt.xlabel('Categoria di Prodotto')
plt.ylabel('Fatturato Netto')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 1. Pulizia una tantum (così non la ripeti per ogni categoria)
iris['Importo_Pulito'] = pd.to_numeric(iris['Importo'].astype(str).str.replace('.00.00', '.00', regex=False), errors='coerce').fillna(0)

# 2. Filtriamo solo i 'Completato'
completati = iris[iris['Status_Ordine'].str.strip() == 'Completato']

# 3. Raggruppiamo direttamente
fatturato_per_categoria = completati.groupby('Categoria_Prodotto')['Importo_Pulito'].sum()

# --- Ora il tuo codice del grafico ---
plt.figure(figsize=(10, 6))
fatturato_per_categoria.sort_values(ascending=False).plot(kind='bar', color='skyblue', edgecolor='navy')

plt.title('Fatturato Netto per Categoria di Prodotto', fontsize=14)
plt.ylabel('Euro (€)')
plt.grid(axis='y', linestyle='--', alpha=0.3)
plt.tight_layout()
plt.show()

# Calcola la percentuale di ogni categoria sul totale
percentuali = (fatturato_per_categoria / fatturato_per_categoria.sum()) * 100
print(percentuali)