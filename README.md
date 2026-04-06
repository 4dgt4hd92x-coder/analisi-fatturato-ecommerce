Analisi Fatturato E-commerce 📊

Progetto Python per l'estrazione e la pulizia di metriche finanziarie da dati grezzi.

## 🎯 Obiettivo
Calcolare il fatturato netto reale filtrando gli ordini "Completati" e risolvendo anomalie di formattazione nei dati sorgente.

## 🛠️ Sfide Tecniche Risolte
- **Data Cleaning Extremo:** Gestione di stringhe numeriche errate (formato `450.00.00`) tramite parsing personalizzato.
- **Validazione Dati:** Gestione dei valori nulli (`NaN`) e degli errori di conversione.
- **Visualizzazione:** Analisi della distribuzione del fatturato per categoria (Elettronica vs Altri).

## 📈 Risultati principali
L'analisi ha rivelato che la categoria **Elettronica** domina il mercato, rappresentando oltre il **60%** del fatturato netto totale, evidenziando una forte dipendenza del business da un singolo settore.

## Tecnologie utilizzate
- Python 3
- Pandas (Manipolazione dati)
- Matplotlib (Visualizzazione)
