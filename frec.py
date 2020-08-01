# Para ejecutarlo solo necesitas tener Pandas, lo instalas con
# python -m pip install pandas
# La ejecución del programa genera un HTML con una tabla en la que 
# puedes ver la frecuencia de las letas.
# Psdt: Aún no soporta caracteres extraños :(

# Versión en desuso.
from string import ascii_lowercase
from collections import Counter



with open('report.txt') as f:
    a = Counter(letter for line in f 
                  for letter in line.lower() 
                  if letter in ascii_lowercase)

print(a)

import pandas as pd
df = pd.DataFrame.from_dict(a, orient='index').reset_index()
df = df.rename(columns={'index':'Word', 0:'Count'})
#print (df)
df.to_html(open('SingleWord.html', 'w'))
