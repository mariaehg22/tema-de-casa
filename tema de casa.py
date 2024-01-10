Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
... import matplotlib.pyplot as plt
... 
... # Citirea datelor din fișierul CSV
... nume_fisier = 'data.csv'
... date = pd.read_csv(nume_fisier)
... 
... # Plotează toate valorile
... date.plot()
... plt.title('Toate valorile')
... plt.show()
... 
... # Plotează primele 9 valori
... X = 8
... date.head(X).plot()
... plt.title(f'Primele {X} valori')
... plt.show()
... 
... # Plotează ultimele 12 valori pentru coloanele Durata și Puls
... Y = 13
... date[['Durata', 'Puls']].tail(Y).plot()
... plt.title(f'Ultimele {Y} valori pentru Durata și Puls')
